"""
Unit tests for the Database class from the main.py file.
The functions of getting flights by airline code are tested,
getting flights between two airports, updating flight information and deleting a flight.
"""

from main import Database
import unittest


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.c = self.db.c

    def test_get_flights_by_airline(self):
        flights = self.db.get_flights_by_airline('AA')
        self.assertIsInstance(flights, list)
        for flight in flights:
            self.assertEqual(flight[2], 'AA')

    def test_get_flights_between_airports(self):
        flights = self.db.get_flights_between_airports('JFK', 'LAX')
        self.assertIsInstance(flights, list)
        for flight in flights:
            self.assertEqual(flight[3], 'JFK')
            self.assertEqual(flight[4], 'LAX')

    def test_update_and_delete_flight(self):
        self.c.execute('''
            INSERT INTO flights (date, airline, origin, destination, departure_time, arrival_time, flight_time, distance)
            VALUES ('2023-01-01', 'AA', 'JFK', 'LAX', 900, 1200, 300, 2500)
        ''')
        new_flight_id = self.c.lastrowid
        self.db.conn.commit()

        new_date = '2023-01-01'
        new_airline = 'DL'
        new_origin = 'LAX'
        new_destination = 'JFK'
        new_departure_time = 1000
        new_arrival_time = 1300
        new_flight_time = 300
        new_distance = 2500

        self.db.update_flights(new_flight_id, new_date, new_airline, new_origin, new_destination, new_departure_time,
                               new_arrival_time, new_flight_time, new_distance)
        self.c.execute('SELECT * FROM flights WHERE id = ?', (new_flight_id,))
        flight = self.c.fetchone()
        self.assertEqual(flight[1], new_date)
        self.assertEqual(flight[2], new_airline)
        self.assertEqual(flight[3], new_origin)
        self.assertEqual(flight[4], new_destination)
        self.assertEqual(flight[5], new_departure_time)
        self.assertEqual(flight[6], new_arrival_time)
        self.assertEqual(flight[7], new_flight_time)
        self.assertEqual(flight[8], new_distance)

        self.db.delete_flights(new_flight_id, new_flight_id)
        self.c.execute('SELECT * FROM flights WHERE id = ?', (new_flight_id,))
        flight = self.c.fetchone()
        self.assertIsNone(flight)
