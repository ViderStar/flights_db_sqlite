import unittest
import test

from Database import Database
from GUI import GUI

if __name__ == '__main__':
    db = Database('flight_data.db')
    db.create_database()

    # LOAD DATA FROM CSV
    db.load_csv_data()

    GUI(db)

    # UPDATE SOME ROWS
    db.update_airports(0, 'LHR', 'London', 'England')
    db.update_airlines(0, 'BA', 'British Airways')
    db.update_flights(0, '2024-01-01', 'BA', 'LHR', 'JFK', 800, 1200, 400, 3500)

    # # TEST BASIC FUNCTIONAL
    # suite = unittest.TestLoader().loadTestsFromModule(test)
    # unittest.TextTestRunner().run(suite)
    #
    # # DELETE ALL ROWS
    # db.delete_airports(0, 50)
    # db.delete_airlines(0, 50)
    # db.delete_flights(0, 50)
