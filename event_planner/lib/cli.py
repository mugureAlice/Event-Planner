import click
from .helpers import *
from . import init_db

init_db()

@click.group()
def cli():
    """Event Planner CLI"""
    pass

# Event commands
@cli.group()
def event():
    pass

@event.command()
@click.option('--name', prompt='Event name')
@click.option('--date', prompt='Event date (YYYY-MM-DD)')
@click.option('--location', prompt='Event location')
@click.option('--description', help='Description')
def add(name, date, location, description):
    event_id = create_event(name, date, location, description)
    click.echo(f"Event created: {event_id}")

@event.command(name='list')
def list_events():
    events = get_all_events()
    for event in events:
        click.echo(f"\nID: {event['id']}, Name: {event['name']}")
        click.echo(f"Date: {event['date']}, Location: {event['location']}")
        if event['description']:
            click.echo(f"Description: {event['description']}")
        click.echo("-" * 30)

@event.command()
@click.argument('event_id', type=int)
def details(event_id):
    event = get_event_by_id(event_id)
    click.echo(f"\nEvent: {event['name']} (ID: {event_id})")
    click.echo(f"Date: {event['date']}, Location: {event['location']}")
    
    rsvps = get_rsvps_for_event(event_id)
    for rsvp in rsvps:
        click.echo(f"Guest: {rsvp['name']} - {rsvp['status']}")

# Guest commands
@cli.group()
def guest():
    pass

@guest.command()
@click.option('--name', prompt='Guest name')
@click.option('--email', prompt='Guest email')
@click.option('--phone', help='Phone')
def add(name, email, phone):
    guest_id = create_guest(name, email, phone)
    click.echo(f"Guest added: {guest_id}")

@guest.command(name='list')
def list_guests():
    guests = get_all_guests()
    for guest in guests:
        click.echo(f"\nID: {guest['id']}, Name: {guest['name']}")
        click.echo(f"Email: {guest['email']}")
        if guest['phone']:
            click.echo(f"Phone: {guest['phone']}")
        click.echo("-" * 30)

# RSVP commands
@cli.group()
def rsvp():
    pass

@rsvp.command()
@click.option('--event-id', prompt='Event ID', type=int)
@click.option('--guest-id', prompt='Guest ID', type=int)
@click.option('--status', type=click.Choice(['Confirmed', 'Declined', 'Pending']), 
              default='Pending')
def add(event_id, guest_id, status):
    rsvp_id = create_rsvp(event_id, guest_id, status)
    click.echo(f"RSVP created: {rsvp_id}")

@rsvp.command()
@click.option('--rsvp-id', prompt='RSVP ID', type=int)
@click.option('--status', prompt='New status', 
              type=click.Choice(['Confirmed', 'Declined', 'Pending']))
def update(rsvp_id, status):
    if update_rsvp_status(rsvp_id, status):
        click.echo(f"Updated to: {status}")
    else:
        click.echo("RSVP not found")

if __name__ == '__main__':
    cli()