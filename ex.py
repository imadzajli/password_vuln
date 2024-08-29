import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Define the SQL injection payload
username = "admin"
password = "' OR 1=1 --"


# Execute the SQL query with raw string interpolation (vulnerable to SQL injection)
cursor.execute(f"SELECT * FROM vuln_user WHERE username = '{username}' and password = '{password}'")

# Fetch all rows from the executed query
rows = cursor.fetchall()

# Print the fetched data
for row in rows:
    print(f"row = {row}")

# Close the connection
conn.close()
