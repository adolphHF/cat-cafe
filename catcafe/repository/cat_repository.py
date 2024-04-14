import shortuuid

class CatRepository:

    def create(data, conn, cursor):
        try:
            cat_data = (shortuuid.uuid(), data['name'], data['age'], data['race'], data['sex'])
            cursor.execute("INSERT INTO cat (id, name, age, race, sex) VALUES (?, ?, ?, ?, ?)", cat_data)
            conn.commit()
        except Exception as e:
            print("Error occurred:", e)

    def getAll(conn, cursor):
        try:
            cursor.execute("SELECT * FROM cat")
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print("Error occurred:", e)
    
    def getOne(id, cursor):
        try:
            cursor.execute("SELECT * FROM cat WHERE id = ?", (id,))
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print("Error occurred:", e)
    
    def delete(id, conn, cursor):
        try:
            cursor.execute("DELETE FROM cat WHERE id = ?", (id,))
            conn.commit()
        except Exception as e:
            print("Error occurred:", e)

    def update(data, id, conn, cursor):
        try:
            cat_data = (data['name'], data['age'], data['race'], data['sex'], id)
            cursor.execute("UPDATE cat SET name = ?, age = ?, race = ?, sex = ? WHERE id = ?", cat_data)
            conn.commit()
        except Exception as e:
            print("Error occurred:", e)
    
    def updateAdopted(is_adopted, id, conn, cursor):
        try:
            cat_data = (is_adopted, id)
            cursor.execute("UPDATE cat SET is_adopted = ? WHERE id = ?", cat_data)
            conn.commit()
        except Exception as e:
            print("Error occurred:", e)