import csv
import random

def generate_dataset(rows, columns):
    with open('fruit_test.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        
        # write the header row
        header = ['Color', 'Diameter', 'Label']
        writer.writerow(header)
        
        # write the data rows
        for i in range(rows):
            color = random.choice(['Green', 'Yellow','Red'])
            diameter = random.randint(1,5)
            fruit = random.choice(['Mango', 'Grape','Lemon'])
            
            row = [color, diameter, fruit]
            writer.writerow(row)

# generate a dataset with 237 rows and 4 columns
generate_dataset(237, 3)