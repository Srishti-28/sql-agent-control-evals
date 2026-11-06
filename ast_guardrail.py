import sqlglot
from sqlglot import exp

class ASTGuardrail:
    def __init__(self, allowed_tables=None):
        self.allowed_tables = allowed_tables or {"financial_metrics"}

    def validate_query(self, query_str: str) -> tuple[bool, str]:
        """
        Parses a SQL query string into an AST using sqlglot, checks for 
        unauthorized table access, and blocks destructive DDL/DML statements.
        Returns (is_safe, reason).
        """
        try:
            parsed_expressions = sqlglot.parse(query_str, read="sqlite")
        except Exception as e:
            return False, f"Syntax Error / Unparsable Query: {str(e)}"

        if not parsed_expressions:
            return False, "Empty query expression."

        for expression in parsed_expressions:
            # 1. Block destructive operations (DROP, DELETE, UPDATE, INSERT, ALTER)
            if isinstance(expression, (exp.Drop, exp.Delete, exp.Update, exp.Insert, exp.Alter)):
                return False, f"Blocked destructive operation: {expression.key.upper()}"

            # 2. Check accessed tables against least-privilege policy
            tables = {t.name.lower() for t in expression.find_all(exp.Table)}
            for table in tables:
                if table and table not in self.allowed_tables:
                    return False, f"Unauthorized table access detected: '{table}'"

        return True, "Query passed AST validation."

if __name__ == "__main__":
    guardrail = ASTGuardrail(allowed_tables={"financial_metrics"})

    # Test 1: Safe query
    print(guardrail.validate_query("SELECT SUM(monthly_budget) FROM financial_metrics;"))
    # Test 2: Injected destructive query
    print(guardrail.validate_query("DROP TABLE financial_metrics;"))
    # Test 3: Unauthorized table access
    print(guardrail.validate_query("SELECT * FROM sensitive_passwords;"))