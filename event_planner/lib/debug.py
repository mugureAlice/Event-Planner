from .helpers import get_all_events, get_all_guests, get_rsvps_for_event
from .seed import seed_database

def test_application():
    
    seed_database()
    
    print("\n=== TESTING APPLICATION ===\n")
    
  
    print("Events:")
    events = get_all_events()
    for event in events:
        print(f"{event['id']}: {event['name']} ({event['date']})")
    
  
    print("\nGuests:")
    guests = get_all_guests()
    for guest in guests:
        print(f"{guest['id']}: {guest['name']} ({guest['email']})")
    
  
    print("\nRSVPs for Event 1:")
    rsvps = get_rsvps_for_event(1)
    for rsvp in rsvps:
        print(f"{rsvp['name']}: {rsvp['status']}")
    
    print("\nAll tests completed successfully")

if __name__ == '__main__':
    test_application()