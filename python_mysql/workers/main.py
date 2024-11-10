import mysql.connector
import dotenv
import os

# Load environment variables from.env file
dotenv.load_dotenv()

host_n=os.getenv("HOST")
#username=os.getenv("USERNAME")
pass_w=os.getenv("PASSWORD")
data_base=os.getenv("DATABASE")



# Connect to the database
db_connection_object = mysql.connector.connect(
    host=host_n,
    user="root",  # Change to your MySQL username
    password=pass_w,  # Change to your MySQL password
    database=data_base  # Change to your database name
)


# Create a cursor object
cursor = db_connection_object.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL
)
""")

# Insert a record
cursor.execute("INSERT INTO users_data (name, age) VALUES (%s, %s)", ("Alice", 30))

# Commit the changes
db_connection_object.commit()

# Retrieve records
cursor.execute("SELECT * FROM users_data")
records = cursor.fetchall()

# Print the records
for record in records:
    print(record)

# Close the cursor and connection
cursor.close()
db_connection_object.close()