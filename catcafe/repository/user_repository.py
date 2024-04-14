class UserRepository:

    def getUser(email, password, cursor):
        try:
            cursor.execute("SELECT * FROM user WHERE email = ? AND password = ?", [email, password])
            user = cursor.fetchall()
            return user
        except Exception as e:
            print("Error occurred:", e)