# SQL Agent Control & Evals (`sql-agent-control-evals`)

A lightweight evaluation sandbox and security guardrail framework designed to test and protect tool-using LLM database agents against **indirect prompt injections**.

## The Problem
When frontier LLMs are connected to production databases via tool-use, untrusted text stored inside legacy columns or user records can act as an indirect prompt injection. If an adversary smuggles instructions into a database row, a naive agent may execute destructive commands (`DROP`, `DELETE`) or perform unauthorized table joins. 

This project implements a **deterministic AI Control layer** combining structural Abstract Syntax Tree (AST) validation with execution-time oversight.

## Repository Structure
- `ast_guardrail.py`: Core safety guardrail using `sqlglot` to parse queries into ASTs and block unauthorized access.
- `database.py`: Mock SQLite database seeded with benign metrics and injection payloads.
- `evaluation_harness.py`: Evaluation test suite.

## Quickstart
```bash
pip install -r requirements.txt
python3 evaluation_harness.py