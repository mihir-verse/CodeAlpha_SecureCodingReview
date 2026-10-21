# Python Security Review

## Project
CodeAlpha Secure Coding Review

## Vulnerability Identified
SQL Injection

## Vulnerable File
vulnerable_code.py

## Problem
The vulnerable example directly concatenates user input
into an SQL query. In a real application, this can allow
crafted input to change the intended SQL query.

## Security Risk
An attacker may manipulate database queries if this
pattern is used in an application connected to a database.

## Recommended Fix
Use parameterized SQL queries instead of string concatenation.

## Secure File
secure_code.py

## Security Improvement
The secure example uses a question-mark placeholder
and passes the username as a separate parameter.

## Testing
The secure example was tested using a temporary,
in-memory SQLite database.

## Conclusion
Parameterized queries help prevent SQL injection by
keeping user input separate from SQL instructions.