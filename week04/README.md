# Lab Quiz 04 - Savings Planner

## Description
A Python program that simulates month-by-month savings growth based on user-defined starting balances, monthly deposits, interest rates, and financial goals. Includes robust input validation and formatting.

## Test Run
- **Inputs:** 
  - Starting Balance: 1000
  - Monthly Deposit: 500
  - Monthly Interest Rate (%): 1
  - Savings Goal: 3000
- **Output:** 
  - Goal reached in 4 months
  - Final Balance: $3070.80
  - Total Interest Earned: $70.80
  *(Matches Acceptance Check 2)*

## Change Made After Testing
- Added `try-except` blocks inside the validation `while` loops to gracefully handle non-numeric inputs and prevent program crashes.