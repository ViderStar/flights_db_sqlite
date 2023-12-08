import csv
from values import airport_values, airline_values, flights_values

with open('data/airports.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "code", "city", "country"])
    for i, airport in enumerate(airport_values):
        writer.writerow([i, airport[0], airport[1], airport[2]])
    print("data/airports.csv has been written!")

with open('data/airlines.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "code", "name"])
    for i, airline in enumerate(airline_values):
        writer.writerow([i, airline[0], airline[1]])
    print("data/airlines.csv has been written!")

with open('data/flights.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(
        ["id", "date", "airline", "origin", "destination", "departure_time", "arrival_time", "flight_time", "distance"])
    for i, flight in enumerate(flights_values):
        writer.writerow([i, flight[0], flight[1], flight[2], flight[3], flight[4], flight[5], flight[6], flight[7]])
    print("data/flights.csv has been written!")