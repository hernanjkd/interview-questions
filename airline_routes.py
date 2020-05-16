from pprint import pprint
from time import time

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


# Solution: find all the airports that don't have any incoming flights, those
# are the connections you need to add because everything else is connected already

arrivals = [route[1] for route in routes]
need_connection = []
for airport in airports:
    if airport not in arrivals:
        need_connection.append(airport)





# data = {}
# for route in routes:
#     if route[0] in data:
#         data[route[0]]['non-stop'].append(route[1])
#     else:
#         data[route[0]] = {'non-stop': [route[1]]}
# departures = data

# for key in departures:
#     for airport in departures[key]['non-stop']:
#         if airport in departures:
#             for port in departures[airport]['non-stop']:
#                 if port != key and port not in departures[key]['non-stop']:
#                     if 'one-stop' in departures[key]:
#                         departures[key]['one-stop'].append(port)
#                     else:
#                         departures[key]['one-stop'] = [port]

# pprint( departures )



# data = {}
# for route in routes:
#     if route[1] in data:
#         data[route[1]].append(route[0])
#     else:
#         data[route[1]] = [route[0]]
# arrivals = data


# def travel(depart, arrive):
#     if arrive in departures[depart]:
#         return [depart, arrive]
    
#     return [depart, *travel(departures[depart][0])]
    

# def get_all_routes(depart):
    
#     # Starting connection
#     start = []
#     if depart in departures:
#         start = departures[depart]
                
#     # Reach all airports
#     airports_reached = {}
#     for airport in airports:
#         if depart == airport:
#             continue
        
#         route = travel(depart, airport)
#         airports_reached[airport] = route

#     return airports_reached

# pprint(get_all_routes('SFO'))

