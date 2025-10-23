import numpy as np
import pandas as pd
import csv

DIM = 5 #dimension of square matrix

# Generate sensor data and write to a file sensor.csv
sensor1 = np.random.randint(0, 10, (DIM, DIM))
sensor2 = np.random.randint(0, 10, (DIM, DIM))

# Write sensor1 data to a file sensor1.csv 
with open('sensor1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sensor1)

# Write sensor2 data to a file sensor2.csv 
with open('sensor2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sensor2)
