import sqlite3

connection = sqlite3.connect('tdlist.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE users(
        idx INTEGER,
        email VARCHAR PRIMARY KEY,
        password VARCHAR(32)    
    );
    """
)

cursor.execute(
    """
    CREATE TABLE todo_list(
        idx INTEGER PRIMARY KEY AUTOINCREMENT,
        user_idx INTEGER,
        content TEXT
    );
    """
)

cursor.execute(
    """
    CREATE TABLE task_list(
        idx INTEGER PRIMARY KEY AUTOINCREMENT,
        todo_idx INTEGER,
        content TEXT
    );
    """
)

connection.commit()
cursor.close()
connection.close()
