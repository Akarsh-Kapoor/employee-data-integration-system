# Employee Data Integration System 🧑‍💻

## Overview :page_facing_up:

This project simulates a real-world employee data integration workflow using Python, REST APIs, SQLite, SQL, and AWS. It demonstrates how enterprise applications exchange, validate, store, and report data in a cloud-hosted environment.

The application:

- Fetches employee data from an external REST API
- Stores employee records in a SQLite database
- Performs data validation checks
- Prevents duplicate record insertion
- Generates city-wise employee reports
- Exports reports to CSV format
- Logs application events and errors
- Handles API failures gracefully
- Deploys and runs on AWS EC2

---

## Tech Stack :pushpin:

- Python
- SQLite
- SQL
- Requests Library
- Pandas
- AWS EC2
- Git & GitHub

---

## Project Structure :memo:

```text
employee-data-integration-system/
│
├── main.py
├── database.py
├── validation.py
├── requirements.txt
├── README.md
├── .gitignore
├── app.log
├── employee_report.csv
└── screenshots/
```

---

## Features :rocket:

### API Integration :zap:

Fetches employee data from the JSONPlaceholder REST API.

### Database Storage :package:

Stores employee information in SQLite with unique constraints.

### Data Validation :white_check_mark:

Validates data quality by identifying duplicate email records.

### Duplicate Prevention :shield:

Uses database constraints and SQL logic to prevent duplicate employee records from being inserted.

### Reporting :chart_with_upwards_trend:

Generates city-wise employee distribution reports using SQL queries.

### CSV Export :file_folder:

Exports generated reports into CSV format for business reporting and analysis.

### Logging & Monitoring :clipboard:

Captures application activity and errors in log files to support troubleshooting and monitoring.

### Cloud Deployment ☁️

Deploys and runs the application on AWS EC2 to simulate a production-style cloud environment.

---

## Sample Workflow :hammer:

```text
External API
     │
     ▼
Python Integration Layer
     │
     ▼
SQLite Database
     │
     ▼
Validation & Quality Checks
     │
     ▼
CSV Report Generation
     │
     ▼
Application Logging
     │
     ▼
AWS EC2 Deployment
```

---

## AWS Deployment ☁️

The application was deployed on an AWS EC2 Ubuntu instance to simulate a cloud-hosted production environment.

### Deployment Steps

1. Created an AWS EC2 Ubuntu instance
2. Connected using EC2 Instance Connect
3. Installed Python, Git, and project dependencies
4. Cloned the GitHub repository
5. Executed:
   - `database.py`
   - `main.py`
   - `validation.py`
6. Generated reports and logs directly on the cloud server

### AWS Services Used

- Amazon EC2
- Security Groups
- Ubuntu Linux

---

## Future Enhancements 🚀

- AWS S3 integration for report storage
- Streamlit dashboard for visualization
- Automated scheduling with cron jobs
- API authentication support
- Email-based report delivery

---

## 🌟 About Me

Hi, I'm **Akarsh Kapoor** — a Data & Analytics professional passionate about solving business problems through technology, automation, and data-driven insights.

This project was built as part of my journey to better understand how APIs, databases, cloud platforms, and automation workflows work together in real-world enterprise environments.

My interests include:

- Data Analytics & Business Intelligence
- SQL & Database Management
- Python Automation
- Cloud Technologies (AWS)
- AI & Data-Driven Solutions

Let's connect!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/akarsh-kapoor/)
