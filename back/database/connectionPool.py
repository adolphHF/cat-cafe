import sqlite3
import queue
import threading
import os

currentDirectory = os.path.abspath(os.path.dirname(__file__))
absolutePath = os.path.join(currentDirectory, "sqliteDB.sqlite3")

class SQLiteConnectionPool:
    def __init__(self, maxConnections=10, database=absolutePath):
        self.maxConnections = maxConnections
        self.database = database
        self.connections = queue.Queue(maxConnections)
        self.lock = threading.Lock()

        for _ in range(maxConnections):
            self.connections.put(self.createConnection())

    def createConnection(self):
        return sqlite3.connect(self.database)

    def getConnection(self):
        with self.lock:
            if not self.connections.empty():
                return self.connections.get()
            else:
                return self.createConnection()

    def releaseConnection(self, conn):
        with self.lock:
            if self.connections.qsize() < self.maxConnections:
                self.connections.put(conn)
            else:
                conn.close()

connectionPool = SQLiteConnectionPool()
