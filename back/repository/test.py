from cat_repository import CatRepository

from connectionPool import connectionPool

conn = connectionPool.getConnection()

cursor = conn.cursor()

print(CatRepository.getAll(conn, cursor))