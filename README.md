# Banking System

A simple Python banking application that models core banking operations — accounts, transactions, and customers — using a clean, layered architecture (models, repositories, services).

## Features

- Create and manage bank accounts
- Deposit and withdraw funds
- Transfer money between accounts
- Transaction history tracking
- Input validation and custom exception handling for invalid operations (e.g. insufficient funds, invalid amounts)
- Data persistence layer for storing accounts/transactions

## Project Structure

```
Banking-System/
├── DB/             # Database setup / connection and persistence logic
├── common/         # Shared constants, enums, and helper utilities used across the app
├── exceptions/      # Custom exception classes for domain-specific error handling
├── models/          # Core domain models (e.g. Account, Customer, Transaction)
├── repositories/     # Data-access layer — CRUD operations for models
├── services/        # Business logic layer (deposits, withdrawals, transfers, etc.)
├── scripts/         # Standalone/setup scripts (e.g. DB initialization, seed data)
├── tests/           # Unit tests for models, repositories, and services
├── utils/           # General-purpose utility functions
├── .gitignore
└── README.md
```

> The project follows a layered design: **models** define the data, **repositories** handle storage/retrieval, and **services** implement the business rules on top of them.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hasnaaabdelrahman/Banking-System.git
   cd Banking-System
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install any dependencies, if a `requirements.txt` is present:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application's entry point script (check the `scripts/` folder for the setup/run script), for example:

```bash
python scripts/create_db.py
```

Adjust the command above to match the actual entry-point file name in your local copy of the repo.

## Running Tests

Unit tests are located in the `tests/` directory. Run them with:

```bash
python -m unittest discover tests
```