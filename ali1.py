import sqlite3
class database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS student(id integer primary key,fname text,lname text,email text,password text)")
        self.con.commit()
    def insert_record(self,fname,lname,email,password):
        self.cur.execute("INSERT INTO student VALUES(NULL,?,?,?,?)",(fname,lname,email,password))
        self.con.commit()
    def select_record(self):
        self.cur.execute("SELECT * FROM student")
        self.con.commit()
    def search_record(self,email,password):
        self.cur.execute("SELECT * FROM student WHERE email=? and password=?",(email,password))
        return self.cur.fetchall()
               
    