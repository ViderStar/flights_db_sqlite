'''
Values for airports and airlines were obtained from the Bureau of Transportation Statistics:
https://www.transtats.bts.gov/DataIndex.asp

Flight data was randomly generated for the purposes of this demonstration.
'''

from random import randint, uniform
from datetime import datetime, timedelta

airport_values = [
    ('LAX', 'Los Angeles', 'California'),
    ('SFO', 'San Francisco', 'California'),
    ('JFK', 'New York', 'New York'),
    ('ATL', 'Atlanta', 'Georgia'),
    ('ORD', 'Chicago', 'Illinois'),
    ('DFW', 'Dallas-Fort Worth', 'Texas'),
    ('DEN', 'Denver', 'Colorado'),
    ('LAS', 'Las Vegas', 'Nevada'),
    ('PHX', 'Phoenix', 'Arizona'),
    ('SEA', 'Seattle', 'Washington'),
    ('MIA', 'Miami', 'Florida'),
    ('BOS', 'Boston', 'Massachusetts'),
    ('MSP', 'Minneapolis', 'Minnesota'),
    ('FLL', 'Fort Lauderdale', 'Florida'),
    ('DTW', 'Detroit', 'Michigan'),
    ('PHL', 'Philadelphia', 'Pennsylvania'),
    ('LGA', 'New York', 'New York'),
    ('BWI', 'Baltimore', 'Maryland'),
    ('SLC', 'Salt Lake City', 'Utah'),
    ('SAN', 'San Diego', 'California'),
    ('DCA', 'Washington', 'District of Columbia'),
    ('MDW', 'Chicago', 'Illinois'),
    ('TPA', 'Tampa', 'Florida'),
    ('HOU', 'Houston', 'Texas'),
    ('PDX', 'Portland', 'Oregon'),
    ('STL', 'St. Louis', 'Missouri'),
    ('BNA', 'Nashville', 'Tennessee'),
    ('OAK', 'Oakland', 'California'),
    ('MCI', 'Kansas City', 'Missouri'),
    ('SMF', 'Sacramento', 'California'),
    ('CLE', 'Cleveland', 'Ohio'),
    ('IND', 'Indianapolis', 'Indiana'),
    ('MKE', 'Milwaukee', 'Wisconsin'),
    ('RDU', 'Raleigh', 'North Carolina'),
    ('SNA', 'Santa Ana', 'California'),
    ('SJU', 'San Juan', 'Puerto Rico'),
    ('HNL', 'Honolulu', 'Hawaii'),
    ('OGG', 'Kahului', 'Hawaii'),
    ('ANC', 'Anchorage', 'Alaska'),
    ('BUF', 'Buffalo', 'New York'),
    ('PIT', 'Pittsburgh', 'Pennsylvania'),
    ('OMA', 'Omaha', 'Nebraska'),
    ('MSY', 'New Orleans', 'Louisiana'),
    ('BDL', 'Hartford', 'Connecticut'),
    ('OKC', 'Oklahoma City', 'Oklahoma'),
    ('ABQ', 'Albuquerque', 'New Mexico'),
    ('BHM', 'Birmingham', 'Alabama'),
    ('ROC', 'Rochester', 'New York'),
    ('TUS', 'Tucson', 'Arizona'),
    ('TUL', 'Tulsa', 'Oklahoma'),
]

airline_values = [
    ('DL', 'Delta Airlines'),
    ('UA', 'United Airlines'),
    ('AA', 'American Airlines'),
    ('WN', 'Southwest Airlines'),
    ('AS', 'Alaska Airlines'),
    ('NK', 'Spirit Airlines'),
    ('G4', 'Allegiant Air'),
    ('B6', 'JetBlue Airways'),
    ('HA', 'Hawaiian Airlines'),
    ('F9', 'Frontier Airlines'),
    ('VX', 'Virgin America'),
    ('SY', 'Sun Country Airlines'),
    ('MQ', 'American Eagle'),
    ('YX', 'Republic Airways'),
    ('OH', 'PSA Airlines'),
    ('9E', 'Endeavor Air'),
    ('YV', 'Mesa Airlines'),
    ('EV', 'ExpressJet'),
    ('QX', 'Horizon Air'),
    ('CP', 'Compass Airlines'),
    ('C5', 'CommutAir'),
    ('ZW', 'Air Wisconsin'),
    ('AX', 'Trans States Airlines'),
    ('PT', 'Piedmont Airlines'),
    ('G7', 'GoJet Airlines'),
    ('KS', 'Peninsula Airways'),
    ('EM', 'Empire Airlines'),
    ('QK', 'Air Canada Jazz'),
    ('PW', 'Precision Air'),
    ('8V', 'Astral Aviation'),
    ('KQ', 'Kenya Airways'),
    ('AT', 'Royal Air Maroc'),
    ('AH', 'Air Algerie'),
    ('AC', 'Air Canada'),
    ('AF', 'Air France'),
    ('AZ', 'Alitalia'),
    ('BA', 'British Airways'),
    ('EI', 'Aer Lingus'),
    ('IB', 'Iberia'),
    ('KL', 'KLM'),
    ('LH', 'Lufthansa'),
    ('SK', 'SAS'),
    ('SN', 'Brussels Airlines'),
    ('VS', 'Virgin Atlantic'),
    ('NH', 'All Nippon Airways'),
    ('JL', 'Japan Airlines'),
    ('QF', 'Qantas'),
    ('SQ', 'Singapore Airlines'),
    ('CX', 'Cathay Pacific'),
    ('KL', 'KLM Royal Dutch Airlines'),
]

flights_values = []
for _ in range(50):
    flight_date = datetime.now() + timedelta(days=randint(-365, 365))
    flight_date = flight_date.strftime('%Y-%m-%d')  # Convert to string in the format YYYY-MM-DD
    airline_code = airline_values[randint(0, len(airline_values) - 1)][0]
    origin_code = airport_values[randint(0, len(airport_values) - 1)][0]
    destination_code = airport_values[randint(0, len(airport_values) - 1)][0]
    departure_time = randint(0, 2400)
    arrival_time = (departure_time + randint(1, 600)) % 2400
    flight_time = randint(1, 16)
    distance = round(uniform(100, 10000), 3)
    # distance = randint(20, 1000)
    flights_values.append(
        (flight_date, airline_code, origin_code, destination_code, departure_time, arrival_time, flight_time,
         distance)
    )
