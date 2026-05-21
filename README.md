# Employee Data Integration System 🧑‍💻

## Overview

This project demonstrates a simple data integration workflow using Python, SQLite, SQL, and REST APIs.

The application:

- Fetches employee data from an external REST API
- Stores employee records in SQLite
- Performs data validation checks
- Generates reports using SQL queries
- Includes error handling for API failures

## Tech Stack :pushpin:

- Python
- SQLite
- SQL
- Requests Library

## Project Structure :memo:
```
employee-data-integration-system/
│
├── main.py
├── database.py
├── validation.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Features :rocket:

### API Integration :zap:

Fetches employee data from JSONPlaceholder API.

### Database Storage :package:

Stores employee information in SQLite.

### Data Validation :white_check_mark:

Checks for duplicate emails.

### Reporting :chart_with_upwards_trend:

Generates city-wise employee counts.

## Sample Workflow :hammer:

API → Python → SQLite → Validation → Reporting
- Automated scheduling
- Authentication support
