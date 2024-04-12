import sys
import shortuuid
from connectionPool import connectionPool

sys.path.insert(0, 'C:/Users/adolh/OneDrive/Escritorio/cat-cafe/back/database')
#Luisen Option sys.path.append('../database')

conn = connectionPool.getConnection()

cursor = conn.cursor()

class CatRepository:

    def create(data):
        try:
            cat_data = (shortuuid.uuid(), data['name'], data['age'], data['race'], data['sex'])
            cursor.execute("INSERT INTO cat (id, name, age, race, sex) VALUES (?, ?, ?, ?, ?)", cat_data)
            conn.commit()
        finally:
            connectionPool.releaseConnection(conn)

    def getAll():
        try:
            cursor.execute("SELECT * FROM cat")
            rows = cursor.fetchall()
            return rows
        finally:
            connectionPool.releaseConnection(conn)
    
    def getOne(id):
        try:
            cursor.execute("SELECT * FROM cat WHERE id = ?", (id,))
            rows = cursor.fetchall()
            return rows
        finally:
            connectionPool.releaseConnection(conn)
    
    def delete(id):
        try:
            cursor.execute("DELETE FROM cat WHERE id = ?", (id,))
            conn.commit()
        finally:
            connectionPool.releaseConnection(conn)

    def update(data, id):
        try:
            cat_data = (data['name'], data['age'], data['race'], data['sex'], id)
            cursor.execute("UPDATE cat SET name = ?, age = ?, race = ?, sex = ? WHERE id = ?", cat_data)
            conn.commit()
        finally:
            connectionPool.releaseConnection(conn)
    
    def updateAdopted(is_adopted, id):
        try:
            cat_data = (is_adopted, id)
            cursor.execute("UPDATE cat SET is_adopted = ? WHERE id = ?", cat_data)
            conn.commit()
        finally:
            connectionPool.releaseConnection(conn)