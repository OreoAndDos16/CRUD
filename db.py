import mariadb

def get_connection():
    try:
        conn = mariadb.connect(
            user="root",           # ⚠️ Replace with your MariaDB username
            password="123",   # ⚠️ Replace with your MariaDB password
            host="localhost",
            port=3306,
            database="employeedb"
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return None
