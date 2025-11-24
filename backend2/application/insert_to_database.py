import datetime
import sqlite3  # or use pymysql / mysql.connector for MySQL
# from models import Reserve_Parking_Spot

# Connect to your database
conn = sqlite3.connect('project_db.sqlite3')  # or use MySQL connection
cursor = conn.cursor()

# Create a datetime object
now = datetime.datetime.now()

# Insert into table
cursor.execute("INSERT INTO Reserve_Parking_Spot (parking_time_stamp) VALUES (?)", (now,))
# For MySQL, use %s instead of ?

conn.commit()
conn.close()