import csv
import random

def generate_dataset(rows, columns):
    with open('system2_test.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        
        # write the header row
        header = ['CacheLevel', 'AccesTime', 'Status']
        writer.writerow(header)
        
        # write the data rows
        for i in range(rows):
            cache = random.choice(['L1', 'L2','L3'])
            access_time = random.randint(1,5)
            status = random.choice(['Leaked', 'NLeaked','Idle'])
            
            row = [cache, access_time, status]
            writer.writerow(row)

# generate a dataset with 500 rows and 3 columns
generate_dataset(500, 3)