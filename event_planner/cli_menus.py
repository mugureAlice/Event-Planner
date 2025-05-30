from database import setup_database
from models import Venue, Event, Guest
from helpers import display_menu, validate_date, validate_email, print_venue, print_event, print_guest, get_int_input
setup_database()

def main_menu():
    menus = {
        '1': ('Venues', lambda: submenu([
            ('Add Venue', add_venue),
            ('List Venues', list_venues),
            ('Delete Venue', delete_venue)
        ])),
        '2': ('Events', lambda: submenu([
            ('Add Event', add_event),
            ('List Events', list_events),
            ('Delete Event', delete_event)
        ])),
        '3': ('Guests', lambda: submenu([
            ('Add Guest', add_guest),
            ('List Guests', list_guests),
            ('Delete Guest', delete_guest)
        ])),
        '4': ('View Event', view_event),
        '5': ('Exit', exit)
    }
    
    while True:
        choice = display_menu([f"{k}. {v[0]}" for k, v in menus.items()])
        menus.get(choice, (None, lambda: print("Invalid choice!")))[1]()

def get_int_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input! Must be a number.")
        return None
def submenu(options):
    choice = display_menu([opt[0] for opt in options])
    if choice in [str(i) for i in range(1, len(options)+1)]:
        options[int(choice)-1][1]()


def add_venue():
    name = input("Venue name: ")
    Venue.create(name, input("Address: "), get_int_input("Capacity: "))

def list_venues(): [print(f"{v[0]}: {v[1]}") for v in Venue.get_all()]

def delete_venue():
    if Venue.delete(get_int_input("Venue ID to delete: ")): print("Deleted!")


def add_event():
    title, date = input("Title: "), input("Date (YYYY-MM-DD): ")
    Event.create(title, input("Description: "), date, get_int_input("Venue ID: "))

def list_events(): [print(f"{e[0]}: {e[1]}") for e in Event.get_all()]

def delete_event():
    if Event.delete(get_int_input("Event ID to delete: ")): print("Deleted!")


def add_guest():
    Guest.create(input("Guest name: "), input("Email: "), get_int_input("Event ID: "))

def list_guests(): [print(f"{g[0]}: {g[1]}") for g in Guest.get_all()]

def delete_guest():
    if Guest.delete(get_int_input("Guest ID to delete: ")): print("Deleted!")


def view_event():
    event = Event.find_by_id(get_int_input("Event ID: "))
    if event: print(f"Event {event[1]} at Venue {event[4]}")