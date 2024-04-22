import mysql.connector
from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler

# Initialize CSV handler
csv_handler = CSVHandler('result_intel.csv')

# Connect to MySQL
def connect_to_mysql():
    # Modify these parameters according to your MySQL setup
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Energy@123',
        'database': 'db'
    }
    return mysql.connector.connect(**db_config)

# Function to execute MySQL query
@measure_energy(handler=csv_handler)
def execute_mysql_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

# Function to prompt user for query input and run the function
def run_mysql_query():
    connection = connect_to_mysql()
    query = input("Enter your MySQL query: ")
    for _ in range(10):
        execute_mysql_query(connection, query)
    connection.close()

# Run the function and save data to CSV
run_mysql_query()
csv_handler.save_data()

