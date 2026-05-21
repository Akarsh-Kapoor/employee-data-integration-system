import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

# Find duplicate emails
cursor.execute("""
SELECT email, COUNT(*)
FROM employees
GROUP BY email
HAVING COUNT(*) > 1
""")

duplicates = cursor.fetchall()

print("Duplicate Emails:")
print(duplicates)

# Generate city report
cursor.execute("""
SELECT city, COUNT(*)
FROM employees
GROUP BY city
""")

report = cursor.fetchall()

print("\nEmployees by City:")
print(report)

# Close only after ALL queries
conn.close()