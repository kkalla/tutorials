CREATE TABLE users(
        idx INTEGER,
        email VARCHAR PRIMARY KEY,
        password VARCHAR(32)    
    );
CREATE TABLE todo_list(
        idx INTEGER PRIMARY KEY AUTOINCREMENT,
        user_idx INTEGER,
        content TEXT
    );
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE task_list(
        idx INTEGER PRIMARY KEY AUTOINCREMENT,
        todo_idx INTEGER,
        content TEXT
    );
