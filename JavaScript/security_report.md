# JavaScript Security Review

## Project
CodeAlpha Secure Coding Review

## Vulnerability Identified
Cross-Site Scripting (XSS) Risk

## Vulnerable File
vulnerable_code.js

## Problem
The vulnerable example inserts user input into the page
using innerHTML. If untrusted input contains HTML or
JavaScript-capable markup, it may create an XSS risk.

## Security Risk
An attacker may be able to inject unwanted content or
execute scripts in the context of a vulnerable website.

## Recommended Fix
Use textContent when displaying untrusted input as plain text.

## Secure File
secure_code.js

## Security Improvement
The secure example uses textContent to display input
without interpreting it as HTML.

## Testing
The vulnerable and secure examples were reviewed by
comparing their DOM manipulation methods.

## Conclusion
Using textContent for plain-text output reduces the
risk associated with inserting untrusted HTML.
