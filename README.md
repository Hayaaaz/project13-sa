# Project 13 — AI Pipeline

This repository contains a small AI application and a full CI/CD pipeline built for Project 13 in System Administration & Maintenance.

## Structure
src/  
tests/  
.github/workflows/  
requirements.txt  

## Bot
A simple deterministic bot that answers:
- Lockdown procedure  
- Fire drill procedure  
- Late policy  

## Tests
Unit tests verify exact responses:
- test_lockdown  
- test_fire_drill  
- test_late_policy  

## Eval Gate
Similarity-based evaluation using:
- eval_cases.json  
- judge.py  
- Threshold: 0.85  
Build fails if average score < 0.85.

## CI/CD
GitHub Actions pipeline:
1. Install dependencies  
2. Lint  
3. Unit tests  
4. Secret scan  
5. Eval gate  

Uses least-privilege permissions:

permissions:

contents: read



## Result
Final CI run passes:
- All steps green  
- Tests pass  
- Eval gate passes  

