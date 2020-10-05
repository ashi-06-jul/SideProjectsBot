import sqlite3


class TeleDB:
    def __init__(self, dbname="todo.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread=False)

    def setup(self):
        tblstmt = "CREATE TABLE IF NOT EXISTS details(Name text, College text, Github text)"
        self.conn.execute(tblstmt)
        self.conn.commit()

    def add_item(self, Name, College, Github):


        stmt = f"INSERT INTO details (Name, College, Github) VALUES (?, ?, ?)"
        args = (Name, College, Github)
        self.conn.execute(stmt, args)
        self.conn.commit()


