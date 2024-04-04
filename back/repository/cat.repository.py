import sys
sys.path.insert(0, 'C:/Users/adolh/OneDrive/Escritorio/cat-cafe/back/database')
#Luisen Option sys.path.append('../database')

from connectionPool import connectionPool

conn = connectionPool.getConnection()

try:
    # Use the connection
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(tables)
finally:
    # Release the connection back to the pool
    connectionPool.releaseConnection(conn)