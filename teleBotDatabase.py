import sqlite3


class TeleDB:
    def __init__(self, dbname="todo.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread=False)

    def setup(self):
        tblstmt = "CREATE TABLE IF NOT EXISTS details(setup text,name text, college text, paid_projects text,os text, ram text, typing text, computer_work text,code text, Experience_level text, Linux text, Programming_language text, Programming_experience text, Framework text, Storage text, Interest text, cmd text, plateform text, showcase text, team_roles text, github text)"
        self.conn.execute(tblstmt)
        self.conn.commit()

    def add_item(self, setup, name, college, paid_projects, os, ram, typing, computer_work, code, Experience_level, Linux, Programming_language, Programming_experience, Framework, Storage, Interest, cmd, plateform, showcase, team_roles, github):


        stmt = "INSERT INTO details (setup, name, college, paid_projects, os, ram, typing, computer_work, code, Experience_level, Linux, Programming_language, Programming_experience, Framework, Storage, Interest, cmd, plateform, showcase, team_roles, github) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = (setup, name, college, paid_projects, os, ram, typing, computer_work, code, Experience_level, Linux, Programming_language, Programming_experience, Framework, Storage, Interest, cmd, plateform, showcase, team_roles, github)
        self.conn.execute(stmt, args)
        self.conn.commit()