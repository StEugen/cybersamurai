# Infrastructure as Code

Systems of configuration control should be:
1. Idempotency - system must not make any changes until need.
2. Guards and Statements - guard act as "fuse", first checks if write, if yes => done, if no => starts Statement. Statement is code that executes to make changes.

