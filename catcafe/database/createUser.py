from connectionPool import ConnectionPool
#import hashlib
import uuid

def create_user(email, password):
    try:
        conn = ConnectionPool.getConnection()
        cursor = conn.cursor()

        # Hashing the password before storing it
        #hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Generating UUID for the user ID
        user_id = str(uuid.uuid4())

        # Insert user data into the user table
        cursor.execute("INSERT INTO user (id, email, password) VALUES (?, ?, ?)", (user_id, email, password))
        
        # Committing the transaction
        conn.commit()
        print("User created successfully!")
    
    except Exception as ex:
        print("Error creating user:", ex)
    
    finally:
        ConnectionPool.releaseConnection(conn)

# Example usage:
create_user("catcafe@admin.com", "password123")