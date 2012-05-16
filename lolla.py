#This file handles requests to the Lolla api
import requests, json

api_key = "2beb11af18abf85a56d9152f54bd3b606feb10b2"

def Call(endpoint):
    def api_call(func):
        def replace_function(*args, **kwargs):
            kwargs['key'] = api_key
            x = requests.get(endpoint % args, params=kwargs)
            return json.loads(x.content)
        replace_function.__doc__ = func.__doc__
        return replace_function
    return api_call


@Call('http://api.dostuffmedia.com/events.json')
def getEvents():
    """
    Returns a dictionary of all events for a festival.
    Optional Fields:
    date: [MM/DD/YY]
    page: [#] for paginiation
    year: [#] for past years

    getEvents(date="10/10/2012", page="1")
    """

@Call('http://api.dostuffmedia.com/events/%s.json')
def getEvent():
    """
    Returns information about a specific event.

    getEvent(1)
    """

@Call('http://api.dostuffmedia.com/events/%s/current_votes.json')
def getEventVotes():
    """
    Returns the number of votes for a specific event.

    getEventVotes(1)
    """

@Call('http://api.dostuffmedia.com/bands.json')
def getBands():
    """
    Returns a dictionary of all bands for a festival.
    page: [#] for paginiation
    year: [#] for past years

    getBands()
    """

@Call('http://api.dostuffmedia.com/bands/%s.json')
def getBand():
    """
    Returns information about a specific band.

    getBand(1)
    """

@Call('http://api.dostuffmedia.com/bands/%s/current_votes.json')
def getBandVotes():
    """
    Returns the number of votes for a specific band.

    getBandVotes(1)
    """

@Call('http://api.dostuffmedia.com/updates.json')
def getUpdates():
    """
    Returns a list of updates and additions to events or bands.

    getUpdates()
    """

@Call('http://api.dostuffmedia.com/venues.json')
def getVenues():
    """
    Returns the entire list of venues.
    page: [#] for paginiation

    getVenues()
    """

@Call('http://api.dostuffmedia.com/venues/%s.json')
def getVenue():
    """
    Returns information about a specific venue.

    getVenue(1)