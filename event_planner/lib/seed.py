from .helpers import create_event, create_guest, create_rsvp
from . import init_db

def seed_database():
    init_db()
    

    events = [
        ("Tech Conference", "2023-12-15", "Convention Center", "Annual tech gathering"),
        ("Product Launch", "2024-01-20", "Downtown Plaza", "New product reveal"),
        ("Company Retreat", "2024-02-10", "Mountain Resort", "Team building activities")
    ]
    
    guests = [
        ("John Doe", "john@gmail.com", "555-1234"),
        ("Jane Smith", "jane@gmail.com", "555-5678"),
        ("Bob Johnson", "bob@gmail.com", "555-9012")
    ]
    

    event_ids = [create_event(*event) for event in events]
    
    
    guest_ids = [create_guest(*guest) for guest in guests]
    
  
    rsvp_data = [
        (0, 0, "Confirmed"), 
        (0, 1, "Pending"),   
        (1, 0, "Declined"),  
        (1, 2, "Confirmed"),  
        (2, 1, "Confirmed")  
    ]
    
 
    for event_idx, guest_idx, status in rsvp_data:
        create_rsvp(event_ids[event_idx], guest_ids[guest_idx], status)
    
    print("Database seeded")

if __name__ == '__main__':
    seed_database()