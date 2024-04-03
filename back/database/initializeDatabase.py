from connectionPool import connectionPool

try:
    conn = connectionPool.getConnection()
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS cat (id CHAR(22) PRIMARY KEY, name VARCHAR(50), age INTEGER, race VARCHAR(50), sex VARCHAR(50), is_adopted TINYINT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS application (id CHAR(22) PRIMARY KEY, cat_id CHAR(22), applicant_name VARCHAR(255), applicant_phone VARCHAR(50), applicant_email VARCHAR(255), applicant_age INTEGER, applicant_address VARCHAR(255), FOREIGN KEY (cat_id) REFERENCES cat(id))")
    cursor.execute("CREATE TABLE IF NOT EXISTS user (id CHAR(22) PRIMARY KEY, email VARCHAR(255), password VARCHAR(255))")
except Exception as ex:
    print(ex)

finally:
    connectionPool.releaseConnection(conn)