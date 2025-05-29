
class Event:
    def __init__(self, id, name, date, location, description=None):
        self.id = id
        self.name = name
        self.date = date
        self.location = location
        self.description = description

class Guest:
    def __init__(self, id, name, email, phone=None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

class RSVP:
    def __init__(self, id, event_id, guest_id, status='Pending'):
        self.id = id
        self.event_id = event_id
        self.guest_id = guest_id
        self.status = status