#  Banking System

A secure and modular Banking System built with **Python** following **Clean Architecture** and **Domain-Driven Design (DDD)** principles. The project provides core banking functionalities such as user authentication, account management, and transaction processing while emphasizing maintainability, scalability, and comprehensive testing.

---

##  Features

- User Registration & Authentication
-  Secure User Login
-  Bank Account Management
-  Deposit Money
-  Withdraw Money
-  Input Validation & Business Rules
-  Custom Exception Handling
-  Behavior-Driven Development (BDD) Testing with Behave
-  Layered Architecture

---

##  Project Architecture

The project follows a clean layered architecture to separate responsibilities.

```
Banking-System/
├── DB/             # Database setup / connection and persistence logic
├── common/         # Shared constants, enums, and helper utilities used across the app
├── exceptions/      # Custom exception classes for domain-specific error handling
├── features/             # BDD feature files
├── models/          # Core domain models (e.g. Account, Customer, Transaction)
├── repositories/     # Data-access layer — CRUD operations for models
├── services/        # Business logic layer (deposits, withdrawals, transfers, etc.)
├── scripts/         # Standalone/setup scripts (e.g. DB initialization, seed data)
├── tests/           # Unit tests for models, repositories, and services
├── utils/           # General-purpose utility functions
├── .gitignore
└── README.md
```

---

##  Tech Stack

- Python 3.10+
- SQLAlchemy
- SQLite
- Behave (BDD)
- Pytest
- Faker
- UUID
- Git & GitHub

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/hasnaaabdelrahman/Banking-System.git

cd Banking-System
```

### 2. Create a virtual environment

Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Running the Application

```bash
python main.py
```

---

##  Running Tests

### Run all unit tests

```bash
pytest
```

### Run a specific test

```bash
pytest tests/
```

### Run all BDD tests

```bash
behave
```

### Run a specific feature

```bash
behave features/login.feature
```


##  Main Functionalities

### Authentication

- Register new users
- Login
- Password validation

### Bank Accounts

- Create account
- Retrieve account information
- Validate account ownership

### Transactions

- Deposit
- Withdraw
- Transfer
- Retrieve transaction history

---

## Design Principles

- Clean Architecture
- SOLID Principles
- Repository Pattern
- Dependency Injection
- Separation of Concerns
- Domain-Driven Design (DDD)

---

## Testing Strategy

This project uses multiple testing approaches:

- Unit Testing (Pytest)
- Behavior-Driven Development (Behave)
- Service Layer Testing
- Repository Testing

---
