import os, dotenv, mysql.connector

dotenv.load_dotenv()

Host=os.getenv("HOST")
passwd=os.getenv("PASSWORD")
db_name=os.getenv("DATABASE")


obj_for_db_connection=mysql.connector.connect(
    host=Host,
    username="root",
    password=passwd,
    database=db_name
)

mysql_query=obj_for_db_connection.cursor()

mysql_query.execute("""
create table if not exists workers(
ID int auto_increment primary key,
NAME VARCHAR(222),
SALARY DECIMAL(10,2));
""")

print("Table created successfully")

mysql_query.execute("""
INSERT INTO workers (NAME, SALARY) VALUES
('John Doe', 50000.00),
('Jane Smith', 60000.50),
('Alice Johnson', 55000.75),
('Bob Brown', 45000.25),
('Charlie Davis', 70000.00);""")

print("Data inserted successfully")

obj_for_db_connection.commit()
#the data will be visible only when the commit operation is done

mysql_query.execute("""
SELECT * FROM workers;
""")


records=mysql_query.fetchall()

for data in records:
    print(data, end="\n")

mysql_query.close()
obj_for_db_connection.close()