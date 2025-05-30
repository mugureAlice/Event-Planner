from database import get_connection

class BaseModel:
    
    
    TABLE_NAME = ""
    COLUMNS = ()
    
    @classmethod
    def _execute(cls, query, params=(), commit=False):
        
        conn = get_connection()
        c = conn.cursor()
        c.execute(query, params)
        if commit:
            conn.commit()
        result = c.lastrowid if "INSERT" in query else c.rowcount > 0 if "DELETE" in query else c.fetchall()
        conn.close()
        return result
    
    @classmethod
    def create(cls, **data):
       
        cols = ", ".join(data.keys())
        placeholders = ", ".join(["?"] * len(data))
        query = f"INSERT INTO {cls.TABLE_NAME} ({cols}) VALUES ({placeholders})"
        return cls._execute(query, tuple(data.values()), commit=True)
    
    @classmethod
    def get_all(cls):
     
        return cls._execute(f"SELECT * FROM {cls.TABLE_NAME}")
    
  
    @classmethod
    def find_by_id(cls, id):
       
        results = cls._execute(f"SELECT * FROM {cls.TABLE_NAME} WHERE id = ?", (id,))
        return results[0] if results else None
    
    @classmethod
    def delete(cls, id):
        return cls._execute(f"DELETE FROM {cls.TABLE_NAME} WHERE id = ?", (id,), commit=True)

class Venue(BaseModel):
    TABLE_NAME = "venues"
    COLUMNS = ("name", "address", "capacity")
    
    @classmethod
    def create(cls, name, address, capacity):
        return super().create(name=name, address=address, capacity=capacity)

class Event(BaseModel):
    TABLE_NAME = "events"
    COLUMNS = ("title", "description", "date", "venue_id")
    
    @classmethod
    def create(cls, title, description, date, venue_id):
        return super().create(title=title, description=description, date=date, venue_id=venue_id)
    
    @classmethod
    def get_guests(cls, event_id):
        
        return cls._execute("SELECT * FROM guests WHERE event_id = ?", (event_id,))

class Guest(BaseModel):
    TABLE_NAME = "guests"
    COLUMNS = ("name", "email", "event_id")
    
    @classmethod
    def create(cls, name, email, event_id):
        return super().create(name=name, email=email, event_id=event_id)