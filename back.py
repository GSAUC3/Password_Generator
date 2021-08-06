import sqlite3 as sq


db='secure.db'
def connect():
    conn=sq.connect(db)
    c=conn.cursor()
    c.execute("""
                 CREATE TABLE IF NOT EXISTS data (
                     site text,
                     user text,
                     password text primary key

                 )              
    """)
    conn.commit()
    conn.close()

def enter(site,user,pas):
    conn= sq.connect(db)
    c=conn.cursor()
    c.execute("INSERT INTO data VALUES(?,?,?)",(site,user,pas))
    conn.commit()
    conn.close() 

def show():
    conn= sq.connect(db)
    c=conn.cursor()
    c.execute("SELECT * FROM data")
    i=c.fetchall()
    conn.commit()
    conn.close()
    return i

def Del(password):
    conn= sq.connect(db)
    c=conn.cursor()
    c.execute("DELETE FROM data WHERE password=(?)",(password,))
    conn.commit()
    conn.close() 

def edit(site,user,password):
    conn= sq.connect(db)
    c=conn.cursor()
    c.execute("UPDATE data SET site=?, user=(?) WHERE password=(?) ",(site,user,password))
    conn.commit()
    conn.close()
    
def check():
    if len(show()) ==0:
        return False
    else:
        return True
connect()
