from pprint import pprint

# Given an airport hub, add the fewest missing connections for the plane
# to be able to reach every other airport. Start: LGA

# All the airports are in the routes

airports = ['BGI','CDG','DEL','DOH','DSM','EWR','EYW','HND','ICN','JFK','LGA',
    'LHR','ORD','SAN','SFO','SIN','TLV','BUD']

routes = [
    ('DSM','ORD'),('ORD','BGI'),('BGI','LGA'),('SIN','CDG'),('CDG','SIN'),
    ('CDG','BUD'),('DEL','DOH'),('DEL','CDG'),('TLV','DEL'),('EWR','HND'),
    ('HND','ICN'),('HND','JFK'),('ICN','JFK'),('JFK','LGA'),('EYW','LHR'),
    ('SFO','SAN'),('SFO','DSM'),('SAN','EYW')
]
#------------------------------------------------------------------------------
data = {}
for route in routes:
    if route[0] in data:
        data[route[0]].append(route[1])
    else:
        data[route[0]] = [route[1]]
routes = data


def travel(depart, arrive):
    if arrive in routes[depart]:
        return [depart, arrive]
    return None

def get_all_routes(depart):
    
    # Starting connection
    start = []
    if depart in routes:
        start = routes[depart]
                
    # Reach all airports
    airports_reached = {}
    for airport in airports:
        if depart == airport:
            continue
        
        route = travel(depart, airport)
        airports_reached[airport] = route

    return airports_reached

pprint(get_all_routes('SFO'))

