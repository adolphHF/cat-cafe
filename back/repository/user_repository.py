class UserRepository:

    def getUser(id, password, conn, cursor):
        try:
            cursor.execute("SELECT * FROM user WHERE id = ?, password = ?", [id, password])
            user = cursor.fetchall()
            return user
        finally:
            connectionPool.releaseConnection(conn)