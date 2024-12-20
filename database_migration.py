from google.cloud import sql
import os

def create_tables(conn):
    """
    Creates the necessary tables in the database.

    Args:
        conn: A database connection object.
    """
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) UNIQUE NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                password_hash VARCHAR(255) NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                title VARCHAR(255) NOT NULL,
                content TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        conn.commit()

def main():
    # Replace with your Cloud SQL instance connection name
    instance_connection_name = "steam-capsule-444320-e6:us-central1:my-app-db" 

    # Get environment variables (more secure)
    db_user = os.environ.get("DB_USER")
   # db_password = os.environ.get("DB_PASSWORD") 

    try:
        # Create a database connection pool
        pool = sql.Pool(
            user=db_user,
            #password=db_password,
            database="myapp_db", 
            instance=instance_connection_name,
            max_connections=5,
            idle_timeout=30,
        )

        with pool.acquire() as conn:
            create_tables(conn)

        print("Tables created successfully.")

    except Exception as e:
        print(f"Error creating tables: {e}")

if __name__ == "__main__":
    main()