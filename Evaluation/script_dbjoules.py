import os
import json
import time
import csv
import psutil
import mysql.connector
import sys
from hardware.ram_metrics import RAM
from hardware.cpu_metrics import CPU

# Function to load parameters
def get_params():
    filename = 'data/config.txt'
    if not os.path.isfile(filename):
        with open(filename, "w"):
            pass
    with open(filename, "r") as json_file:
        if os.path.getsize(filename):
            dictionary = json.loads(json_file.read())
        else:
            dictionary = {
                "project_name": "project name",
                "file_name": "emission.csv",
                "measure_period": 10,
                "pue": 1,
            }
    return dictionary

# Function to execute MySQL query
def execute_mysql_query(query):
    try:
        cnx = mysql.connector.connect(user='root', password='Energy@123', host='localhost', database='db')
        cursor = cnx.cursor()

        start_time = time.time()  # Start timing the query execution
        cursor.execute(query)
        results = cursor.fetchall()
        end_time = time.time()  # End timing the query execution

        cursor.close()
        cnx.close()
        
        # Calculate query duration
        duration = end_time - start_time
        return results, duration
    except mysql.connector.Error as err:
        print("Error executing MySQL query:", err)
        return None, None

# Function to save data to CSV
class CSVHandler:
    def __init__(self, filename):
        self.filename = filename

    def save_data(self, query, data):
        file_exists = os.path.isfile(self.filename)
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                headings = ['Query', 'CPU Energy Consumption (Joules)', 'RAM Energy Consumption (Joules)', 'Total Energy Consumption (Joules)', 'Query Duration (seconds)']
                writer.writerow(headings)
            writer.writerow([query] + data)

def main():
    # Load parameters
    params_dict = get_params()
    pue = params_dict.get("pue", 1)

    # Initialize RAM and CPU objects
    ram_monitor = RAM()
    cpu_monitor = CPU()

    # Get MySQL query from user input
    query = input("Enter MySQL query: ")

    # Execute MySQL query 10 times
    for i in range(10):
        print(f"Running query {i+1}/10...")
        
        # Execute MySQL query
        start_ram_consumption = ram_monitor.get_consumption()
        #start_cpu_consumption = psutil.cpu_percent(interval=1)
        query_results, query_duration = execute_mysql_query(query)
            
        end_ram_consumption = ram_monitor.get_consumption()
        end_cpu_consumption = psutil.cpu_percent(interval=1)

        # Calculate CPU and RAM energy consumption
        cpu_energy = (end_cpu_consumption)
        ram_energy = (end_ram_consumption - start_ram_consumption)
        # Total energy consumption
        total_energy_consumption = cpu_energy + ram_energy

        # Save data to CSV
        csv_handler = CSVHandler('result_dbjoules.csv')
        csv_data = [cpu_energy * pue, ram_energy * pue, total_energy_consumption * pue, query_duration]
        csv_handler.save_data(query, csv_data)

        #print("CPU Energy Consumption:", cpu_energy * pue, "Joules")
        #print("RAM Energy Consumption:", ram_energy * pue, "Joules")
        #print("Total Energy Consumption:", total_energy_consumption * pue, "Joules")
        #print("Query Duration:", query_duration, "seconds")
        
if __name__ == "__main__":
    main()

