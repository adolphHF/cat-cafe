import shortuuid

class ApplicationRepository:

    def create(data, conn, cursor):
        try:
            application_data = (shortuuid.uuid(), data['cat_id'], data['applicant_name'], data['applicant_phone'], data['applicant_email'], data['applicant_age'], data['applicant_address'])
            cursor.execute("INSERT INTO application (id, cat_id, applicant_name, applicant_phone, applicant_email, applicant_age, applicant_address) VALUES (?, ?, ?, ?, ?, ?, ?)", application_data)
            conn.commit()
        except Exception as e:
            print("Error occurred:", e)

    def getAll(conn, cursor):
        try:
            cursor.execute("SELECT * FROM application")
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print("Error occurred:", e)
    
    def delete(id, conn, cursor):
        try:
            cursor.execute("DELETE FROM application WHERE id = ?", (id,))
            conn.commit()
        except Exception as e:
            print("Error occurred:", e)
    
    def updateStatus(status, id, conn, cursor):
        try:
            application_data = (status, id)
            cursor.execute("UPDATE application SET status = ? WHERE id = ?", application_data)
            conn.commit()
        except Exception as e:
            print("Error occurred:", e)