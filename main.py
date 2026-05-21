import requests
import sqlite3

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        conn = sqlite3.connect("employees.db")
        cursor = conn.cursor()

        for user in data:

            cursor.execute("""
            INSERT INTO employees (id, name, email, city)
            VALUES (?, ?, ?, ?)
            """, (
                user['id'],
                user['name'],
                user['email'],
                user['address']['city']
            ))

        conn.commit()
        conn.close()

        print("Data Inserted Successfully")

    else:
        print(f"API Error: {response.status_code}")

except Exception as e:
    print("Something went wrong:", e)