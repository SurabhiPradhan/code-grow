import sqlite3


def connection():
    con = sqlite3.connect("Books.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (title TEXT, year INTEGER, rating REAL, author TEXT, isbn INTEGER NOT NULL PRIMARY KEY , summary TEXT)")
    con.commit()
    con.close()


def insert(title,year,rating,author,isbn, summary):
    con = sqlite3.connect("Books.db")
    cur = con.cursor()
    cur.execute("INSERT INTO booky VALUES (?,?,?,?,?,?)",(title,year,rating,author,isbn, summary))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("Books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM booky")
    results = cur.fetchall()
    con.close()
    return results

def search(title="",year="",author="",isbn=""):
    con = sqlite3.connect("Books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM booky WHERE title=? OR year=? OR author=? OR isbn=?",(title,year,author,isbn))
    results = cur.fetchall()
    con.close()
    return results


def delete(isbn):
    con = sqlite3.connect("Books.db")
    cur = con.cursor()
    cur.execute("DELETE FROM booky WHERE isbn=?",(isbn,))
    con.commit()
    con.close()

def update(title,year,rating,author,summary,isbn):
    con = sqlite3.connect("Books.db")
    cur = con.cursor()
    cur.execute("UPDATE booky SET title=?, year=?, rating=?, author=?, summary=? WHERE isbn=?", (title,year,rating,author,summary,isbn))
    con.commit()
    con.close()


connection()
#update("Time",1987,6.1,"SK.W","Drama",90020205)
#insert("Theory of Everything", 1969, 8, "Stephen hawking", 90020207, "Time as 4th Dimension,and its correlation with Blackholes")
#delete(90020203)
#print(view())
#print(search(author="Admand"))
