FINTECH LEDGER SYSTEM

This is a core banking engine system

## Table of content

- Features
- Installation
- System Design
- Usage
- Endpoints
- Email notifications
- Bank statement download
- Tech Stack
- Contributions
- License
- Author

transfer_Funds:

- starts atomic block
- checks transaction if idempotency key exists
- lock both accounts: row level locking
- checks sender balance
- creates transaction record
- create two ledger entry rows
- verify sum of entries
- update account balance
- Database indexing
- Balance Computation
