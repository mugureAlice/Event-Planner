from datetime import date

def display_menu(options):
    
    print(f"\n{'='*30}\n" + "\n".join(f"{i}. {opt}" for i, opt in enumerate(options, 1)) + f"\n{'='*30}")
    return input("Enter your choice: ")

def validate_date(d):
   
    try:
        date.fromisoformat(d)
        return True
    except:
        return False

def validate_email(e):
   
    return "@" in e and "." in e.split("@", 1)[-1]

def print_venue(v):

    print(f"ID: {v[0]}, Name: {v[1]}\nAddress: {v[2]}, Capacity: {v[3]}\n{'-'*20}")

def print_event(e):
    
    print(f"ID: {e[0]}, Title: {e[1]}\nDate: {e[3]}\n{'-'*20}")

def print_guest(g):
    
    print(f"ID: {g[0]}, Name: {g[1]}\nEmail: {g[2]}\n{'-'*20}")
    
def get_int_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input! Must be a number.")
        return None    