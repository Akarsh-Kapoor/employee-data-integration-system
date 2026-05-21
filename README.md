# Employee Data Integration System

## Overview

This project demonstrates a simple data integration workflow using Python, SQLite, SQL, and REST APIs.

The application:

- Fetches employee data from an external REST API
- Stores employee records in SQLite
- Performs data validation checks
- Generates reports using SQL queries
- Includes error handling for API failures
- Can be deployed on AWS EC2

## Tech Stack

- Python
- SQLite
- SQL
- Requests Library
- AWS EC2 (Optional Deployment)

## Project Structure

employee-data-integration-system/
│
├── main.py
├── database.py
├── validation.py
├── requirements.txt
├── README.md
└── .gitignore

## Features

### API Integration

Fetches employee data from JSONPlaceholder API.

### Database Storage

Stores employee information in SQLite.

### Data Validation

Checks for duplicate emails.

### Reporting

Generates city-wise employee counts.

## Sample Workflow

API → Python → SQLite → Validation → Reporting

## Future Improvements

- AWS S3 integration
- Streamlit dashboard
- Automated scheduling
- Authentication support
