import sqlite3

def get_db_connection():
    conn = sqlite3.connect('event_planner.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        date TEXT NOT NULL,
        location TEXT NOT NULL,
        description TEXT
    )
    ''')
    
  
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS guests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT
    )
    ''')
    
  
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rsvps (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_id INTEGER NOT NULL,
        guest_id INTEGER NOT NULL,
        status TEXT DEFAULT 'Pending',
        FOREIGN KEY (event_id) REFERENCES events (id),
        FOREIGN KEY (guest_id) REFERENCES guests (id)
    )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()