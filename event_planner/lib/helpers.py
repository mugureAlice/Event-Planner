from . import get_db_connection


def create_event(name, date, location, description=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO events (name, date, location, description)
    VALUES (?, ?, ?, ?)
    ''', (name, date, location, description))
    conn.commit()
    event_id = cursor.lastrowid
    conn.close()
    return event_id

def get_all_events():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM events')
    events = cursor.fetchall()
    conn.close()
    return events

def get_event_by_id(event_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM events WHERE id = ?', (event_id,))
    event = cursor.fetchone()
    conn.close()
    return event


def create_guest(name, email, phone=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO guests (name, email, phone)
    VALUES (?, ?, ?)
    ''', (name, email, phone))
    conn.commit()
    guest_id = cursor.lastrowid
    conn.close()
    return guest_id

def get_all_guests():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM guests')
    guests = cursor.fetchall()
    conn.close()
    return guests


def create_rsvp(event_id, guest_id, status='Pending'):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO rsvps (event_id, guest_id, status)
    VALUES (?, ?, ?)
    ''', (event_id, guest_id, status))
    conn.commit()
    rsvp_id = cursor.lastrowid
    conn.close()
    return rsvp_id

def get_rsvps_for_event(event_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT rsvps.id, guests.name, guests.email, rsvps.status 
    FROM rsvps 
    JOIN guests ON rsvps.guest_id = guests.id 
    WHERE rsvps.event_id = ?
    ''', (event_id,))
    rsvps = cursor.fetchall()
    conn.close()
    return rsvps

def update_rsvp_status(rsvp_id, status):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE rsvps 
    SET status = ? 
    WHERE id = ?
    ''', (status, rsvp_id))
    conn.commit()
    updated = cursor.rowcount > 0
    conn.close()
    return updated