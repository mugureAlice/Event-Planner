# from .helpers import create_event, create_guest, create_rsvp
# from . import init_db

# def seed_database():
#     # Initialize database
#     init_db()
    
#     # Create events
#     events = [
#         ("Tech Conference", "2023-12-15", "Convention Center", "Annual tech gathering"),
#         ("Product Launch", "2024-01-20", "Downtown Plaza", "New product reveal"),
#         ("Company Retreat", "2024-02-10", "Mountain Resort", "Team building activities")
#     ]
    
#     event_ids = []
#     for event in events:
#         event_id = create_event(*event)
#         event_ids.append(event_id)
    
#     # Create guests
#     guests = [
#         ("John Doe", "john@example.com", "555-1234"),
#         ("Jane Smith", "jane@example.com", "555-5678"),
#         ("Bob Johnson", "bob@example.com", "555-9012")
#     ]
    
#     guest_ids = []
#     for guest in guests:
#         guest_id = create_guest(*guest)
#         guest_ids.append(guest_id)
    
#     # Create RSVPs
#     rsvps = [
#         (event_ids[0], guest_ids[0], "Confirmed"),
#         (event_ids[0], guest_ids[1], "Pending"),
#         (event_ids[1], guest_ids[0], "Declined"),
#         (event_ids[1], guest_ids[2], "Confirmed"),
#         (event_ids[2], guest_ids[1], "Confirmed")
#     ]
    
#     for rsvp in rsvps:
#         create_rsvp(*rsvp)
    
#     print("✅ Database seeded with sample data")

# if __name__ == '__main__':
#     seed_database()

