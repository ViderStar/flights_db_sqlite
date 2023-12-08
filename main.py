import sqlite3
import pandas as pd
import os
import unittest
import test
from values import airport_values, airline_values, flights_values


class Database:
    def __init__(self):
        """
        Initialize Database class.
        Establishes a SQLite connection and creates a cursor.
        """
        self.conn = sqlite3.connect('flights_db.sqlite')
        self.c = self.conn.cursor()

    def create_database(self):
        """
        Creates tables in the database for airports, airlines, and flights.
        """
        c = self.conn.cursor()
        # self.conn.execute("PRAGMA foreign_keys = 1")
        c.execute('''
            DROP TABLE IF EXISTS airports;
        ''')

        c.execute('''
            CREATE TABLE airports (
                id INTEGER PRIMARY KEY,
                code TEXT,
                city TEXT NOT NULL,
                country TEXT NOT NULL
            );
        ''')

        c.execute('''
            DROP TABLE IF EXISTS airlines;
        ''')

        c.execute('''
            CREATE TABLE airlines (
                id INTEGER PRIMARY KEY,
                code TEXT,
                name TEXT NOT NULL
            );
        ''')

        c.execute('''
            DROP TABLE IF EXISTS flights;
        ''')

        c.execute('''
            CREATE TABLE flights (
                id INTEGER PRIMARY KEY,
                date TEXT NOT NULL,
                airline TEXT,
                origin TEXT,
                destination TEXT,
                departure_time INTEGER,
                arrival_time INTEGER,
                flight_time INTEGER,
                distance INTEGER,
                FOREIGN KEY (airline) REFERENCES airlines(code),
                FOREIGN KEY (origin) REFERENCES airports(code),
                FOREIGN KEY (destination) REFERENCES airports(code)
            );
        ''')

        self.conn.commit()

    def load_data(self):
        """
        Loads data from CSV files into the airports, airlines, and flights tables.
        """
        conn = self.conn

        if os.path.exists('data/airports.csv'):
            try:
                airports = pd.read_csv('data/airports.csv')
                airports.to_sql('airports', conn, if_exists='append', index=False)
            except pd.errors.ParserError:
                print('Error reading airports.csv')
        else:
            print('airports.csv not found')

        if os.path.exists('data/airlines.csv'):
            try:
                airlines = pd.read_csv('data/airlines.csv')
                airlines.to_sql('airlines', conn, if_exists='append', index=False)
            except pd.errors.ParserError:
                print('Error reading airlines.csv')
        else:
            print('airlines.csv not found')

        if os.path.exists('data/flights.csv'):
            try:
                flights = pd.read_csv('data/flights.csv')
                flights.to_sql('flights', conn, if_exists='append', index=False)
            except pd.errors.ParserError:
                print('Error reading flights.csv')
        else:
            print('flights.csv not found')

        self.conn.commit()

    def insert_airports(self, airport_values):
        """
        Inserts the given airport values into the airports table.
        """

        for i, airport in enumerate(airport_values):
            self.c.execute(
                f'''
                INSERT INTO airports (id, code, city, country) 
                VALUES ({i}, '{airport[0]}', '{airport[1]}', '{airport[2]}');
            ''')

        self.conn.commit()

    def insert_airlines(self, airline_values):
        """
        Inserts the given airline values into the airlines table.
        """
        for i, airline in enumerate(airline_values):
            self.c.execute(
                f'''
                INSERT INTO airlines (id, code, name) 
                VALUES ({i}, '{airline[0]}', '{airline[1]}');
            ''')

        self.conn.commit()

    def insert_flights(self, flights_values):
        """
        Inserts the given flight values into the flights table.
        """
        for i, flight in enumerate(flights_values):
            self.c.execute(
                f'''
                INSERT INTO flights 
                (id, date, airline, origin, destination, departure_time, arrival_time, flight_time, distance) 
                VALUES ({i}, '{flight[0]}', '{flight[1]}', '{flight[2]}', '{flight[3]}', {flight[4]}, 
                        {flight[5]}, {flight[6]}, {flight[7]});
                ''')

        self.conn.commit()

    def get_flights_by_airline(self, airline_code):
        """
        Returns all flights by the given airline code.
        """
        c = self.conn.cursor()

        c.execute('''
            SELECT *
            FROM flights
            INNER JOIN airlines ON flights.airline = airlines.code
            WHERE airlines.code = ?
        ''', (airline_code,))

        return c.fetchall()

    def get_flights_between_airports(self, origin_code, destination_code):
        """
        Returns all flights between the given origin and destination airports.
        """
        c = self.conn.cursor()

        c.execute('''
            SELECT *
            FROM flights
            INNER JOIN airports AS origin_airports ON flights.origin = origin_airports.code
            INNER JOIN airports AS destination_airports ON flights.destination = destination_airports.code
            WHERE origin_airports.code = ? AND destination_airports.code = ?
        ''', (origin_code, destination_code))

        return c.fetchall()

    def update_airports(self, id, code, city, country):
        """
        Updates an airport with the given id.
        """
        self.c.execute('''
            UPDATE airports
            SET code = ?, city = ?, country = ?
            WHERE id = ?
        ''', (code, city, country, id))

        self.conn.commit()

    def update_airlines(self, id, code, name):
        """
        Updates an airline with the given id.
        """
        self.c.execute('''
            UPDATE airlines
            SET code = ?, name = ?
            WHERE id = ?
        ''', (code, name, id))

        self.conn.commit()

    def update_flights(self, id, date, airline, origin, destination, departure_time, arrival_time, flight_time,
                       distance):
        """
        Updates a flight with the given id.
        """
        self.c.execute('''
            UPDATE flights
            SET date = ?, airline = ?, origin = ?, destination = ?, departure_time = ?, arrival_time = ?, flight_time = ?, distance = ?
            WHERE id = ?
        ''', (date, airline, origin, destination, departure_time, arrival_time, flight_time, distance, id))

        self.conn.commit()

    def delete_airports(self, id_start, id_end):
        """
        Deletes airports with ids in the given range.
        """
        self.c.execute('DELETE FROM airports WHERE id BETWEEN ? AND ?', (id_start, id_end))
        self.conn.commit()

    def delete_airlines(self, id_start, id_end):
        """
        Deletes airlines with ids in the given range.
        """
        self.c.execute('DELETE FROM airlines WHERE id BETWEEN ? AND ?', (id_start, id_end))
        self.conn.commit()

    def delete_flights(self, id_start, id_end):
        """
        Deletes flights with ids in the given range.
        """
        self.c.execute('DELETE FROM flights WHERE id BETWEEN ? AND ?', (id_start, id_end))
        self.conn.commit()

    def drop_db(self, password):
        """
        Drops the database if the correct password is provided.
        """
        if password == 'your_password':
            self.c.execute('''
                DROP TABLE IF EXISTS airports;
            ''')
            self.c.execute('''
                DROP TABLE IF EXISTS airlines;
            ''')
            self.c.execute('''
                DROP TABLE IF EXISTS flights;
            ''')
            self.conn.commit()
            print("Database dropped successfully.")
        else:
            print("Incorrect password. Database was not dropped.")


if __name__ == '__main__':
    db = Database()
    # db.drop_db('your_password')

    db.create_database()

    # LOAD DATA FROM CSV
    db.load_data()

    # INSERT 50 ROWS
    # db.insert_airports(airport_values)
    # db.insert_airlines(airline_values)
    # db.insert_flights(flights_values)

    # UPDATE SOME ROWS
    # db.update_airports(0, 'LHR', 'London', 'England')
    # db.update_airlines(0, 'BA', 'British Airways')
    # db.update_flights(0, '2024-01-01', 'BA', 'LHR', 'JFK', 800, 1200, 400, 3500)

    # TEST BASIC FUNCTIONAL
    # suite = unittest.TestLoader().loadTestsFromModule(test)
    # unittest.TextTestRunner().run(suite)

    # DELETE ALL ROWS
    # db.delete_airports(0, 50)
    # db.delete_airlines(0, 50)
    # db.delete_flights(0, 50)
