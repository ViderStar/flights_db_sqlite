# Flight Database Management
This project is a Python-based application for managing a SQLite database of flights, airlines, and airports. It allows you to create, read, update, and delete data from the database. The database consists of three tables: airports, airlines, and flights.

## Functionality
The Database class provides the following methods:

- create_database: creates the airports, airlines, and flights tables.
- insert_airports, insert_airlines, insert_flights: insert data into the respective tables.
- load_data: loads data from CSV files into the respective tables.
- get_flights_by_airline, get_flights_between_airports: fetch flights based on airline code or origin and destination airports.
- update_airports, update_airlines, update_flights: update records in the respective tables.
- delete_airports, delete_airlines, delete_flights: delete records in the respective tables.

## Installation and Use
1. Ensure Python 3.8 or later is installed on your system.

2. Clone this repository to your local machine.

3. Install the required packages listed in requirements.txt using pip:

```bash
pip install -r requirements.txt
```
4. Run main.py to use the application. Note that running main.py will:

5. Create a SQLite database called flights_db.sqlite if it does not exist.
6. Create tables and insert some records.
7. Update some records.
8. Run unit tests.
9. Finally, delete all the inserted records.

## Testing
Unit tests are included in the test.py file. They test the functions of getting flights by airline code, getting flights between two airports, updating flight information, and deleting a flight.

## Data
Data for airports and airlines is stored in values.py. The airport_values and airline_values variables contain data for 50 airports and airlines respectively. The flights_values variable contains randomly generated flight data. The actual data for airports, airlines, and flights is expected to be loaded from CSV files using the load_data method.

## Notes
- The load_data function expects the CSV files to be in the same directory as the script. The names of the files are airports.csv, airlines.csv, and flights.csv.
- The data in the CSV files should have the same structure as the data in the values.py file.
- The load_data function will append the data from the CSV files to the existing data in the tables.
- The delete functions take a range of IDs to delete. Be careful with these functions as they will permanently delete data from the database.