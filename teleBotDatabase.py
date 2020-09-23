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




    # def get_items(self, owner):
    #     try:
    #         stmt = "SELECT * FROM details WHERE Chat_id = (?)"
    #         args = (owner,)
    #         return [x[1:] for x in self.conn.execute(stmt, args)][0]
    #     except:
    #         return 'error'

