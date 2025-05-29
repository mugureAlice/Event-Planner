import uuid


class User:
    def __init__(self, name: str, email: str, id: str = None):
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.email = email

class Schedule:
    def __init__(self, title: str, location: str, time: str, user_id: str, id: str = None):
        self.id = id or str(uuid.uuid4())
        self.title = title
        self.location = location
        self.time = time  
        self.user_id = user_id

class Attendee:
    def __init__(self, name: str, email: str, schedule_id: str, id: str = None):
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.email = email
        self.schedule_id = schedule_id
