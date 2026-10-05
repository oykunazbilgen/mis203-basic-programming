# Lab 03 - Order Approval Policy

This folder contains the Python script and test cases for Lab 03.

## Test Table (Boundary Cases)

| Test Case | Requested Qty | Available Stock | Order Amount (TRY) | Is Member? | Expected Result | Actual Result |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Below Threshold (499.99 TRY)** | 1 | 10 | 499.99 | Yes | Approved - No discount (499.99 TRY) | Passed |
| **Exact Threshold (500.00 TRY)** | 1 | 10 | 500.00 | Yes | Approved - 10% Discount (450.00 TRY) | Passed |
| **Above Threshold (500.01 TRY)** | 1 | 10 | 500.01 | Yes | Approved - 10% Discount (450.01 TRY) | Passed |
| **Error Case (Insufficient Stock)**| 15 | 10 | 600.00 | Yes | Rejected - No final price shown | Passed |

## Test Run & Code Update Note

* **Test Ran:** I tested the system with a requested quantity of `0` and a negative quantity (`-5`).
* **Change Made:** Initially, invalid quantities could bypass the stock check if the stock was positive. After testing, I added the condition `if requested_quantity <= 0:` at the top of the decision block to ensure invalid requests are immediately rejected with an error message before processing the stock or discount logic.