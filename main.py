import requests
import sqlite3
import logging

# Configure Logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

url = "https://jsonplaceholder.typicode.com/users"

try:

    logging.info("API request started")

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        conn = sqlite3.connect("employees.db")
        cursor = conn.cursor()

        for user in data:

            cursor.execute("""
            INSERT OR IGNORE INTO employees (id, name, email, city)
            VALUES (?, ?, ?, ?)
            """, (
                user['id'],
                user['name'],
                user['email'],
                user['address']['city']
            ))

        conn.commit()

        logging.info("Employee data inserted successfully")

        print("Data Inserted Successfully")

        conn.close()

    else:

        logging.error(
            f"API returned status code {response.status_code}"
        )

        print("API Error")

except Exception as e:

    logging.error(
        f"Application failed: {e}"
    )

    print("Something went wrong:", e)