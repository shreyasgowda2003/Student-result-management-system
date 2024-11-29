import sqlite3

def create_db():
    conn = sqlite3.connect(database="ResultManagementSystem.db")
    cur = conn.cursor()

    # Table Creation for Course Page
    cur.execute("CREATE TABLE IF NOT EXISTS course("
                "cid INTEGER PRIMARY KEY AUTOINCREMENT,"
                "name TEXT,"
                "duration TEXT,"
                "charges TEXT,"
                "description TEXT)"
                )
    
    # Table Creation for Student Page
    cur.execute("CREATE TABLE IF NOT EXISTS student("
                "roll INTEGER PRIMARY KEY AUTOINCREMENT,"
                "name TEXT,"
                "email TEXT,"
                "gender TEXT,"
                "dob TEXT,"
                "contact TEXT,"
                "admission TEXT,"
                "course TEXT,"
                "state TEXT,"
                "city TEXT,"
                "pin TEXT,"
                "address TEXT)"
                )

    # Table Creation for Result Page
    cur.execute("CREATE TABLE IF NOT EXISTS result("
                "rid INTEGER PRIMARY KEY AUTOINCREMENT,"
                "roll TEXT,"
                "name TEXT,"
                "course TEXT,"
                "marks_obtain TEXT,"
                "full_marks TEXT,"
                "percentage TEXT)"
                )

    # Table Creation for Sign_Up Page
    cur.execute("CREATE TABLE IF NOT EXISTS AllUsers("
                "eid INTEGER PRIMARY KEY AUTOINCREMENT,"
                "f_name TEXT,"
                "l_name TEXT,"
                "contact TEXT,"
                "email TEXT,"
                "question TEXT,"
                "answer TEXT,"
                "password TEXT,"
                "u_name TEXT)"
                )

    # Table Creation for Graph
    cur.execute("CREATE TABLE IF NOT EXISTS graph("
                "gid INTEGER PRIMARY KEY AUTOINCREMENT,"
                "data_type TEXT,"
                "data_value TEXT)"
                )

    conn.commit()
    conn.close()

create_db()
