# Evaluating AI Control & Adversarial Robustness in Tool-Using SQL Agents (`sql-agent-control-evals`)

## Overview
This repository contains an empirical evaluation harness designed to test how tool-using Large Language Model (LLM) database agents handle **indirect prompt injections** embedded within untrusted database records, and evaluates a lightweight **AI Control monitoring scaffold** to prevent unauthorized database modifications or table exfiltration.

## Motivation & Threat Model
Autonomous enterprise AI agents are increasingly granted tool access to relational databases and microservices. When an agent queries external or user-generated data (e.g., customer feedback rows, support tickets, or web scraped text), malicious inputs can contain hidden instructions that hijack the agent's control flow.

This project investigates:
1. **Indirect Prompt Injection:** How malicious strings embedded in SQL text fields trick agents into executing unauthorized commands (e.g., `DROP TABLE`, `UNION SELECT` credential dumps).
2. **Untrusted Monitoring & AI Control:** Evaluating a lightweight secondary guardrail that intercepts generated SQL Abstract Syntax Trees (ASTs) before execution against strict safety policies.

## Repository Structure
- `eval_harness.py`: Main evaluation script containing a mock SQLite database, injection test cases, simulated agent queries, and a deterministic safety control monitor.

## Running the Evaluation Locally
No paid API keys or external services are required. The script runs entirely locally using Python standard libraries and SQLite.

```bash
python eval_harness.py
