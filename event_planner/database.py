import sqlite3

def setup_database():
    conn = sqlite3.connect('event_planner.db')
    c = conn.cursor()
    
    
    c.execute('''CREATE TABLE IF NOT EXISTS venues (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 address TEXT,
                 capacity INTEGER
                 )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS events (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 title TEXT NOT NULL,
                 description TEXT,
                 date TEXT,
                 venue_id INTEGER,
                 FOREIGN KEY(venue_id) REFERENCES venues(id)
                 )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS guests (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 email TEXT,
                 event_id INTEGER,
                 FOREIGN KEY(event_id) REFERENCES events(id)
                 )''')
    
    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect('event_planner.db')