import csv
import random

def generate_dataset(rows, columns):
    with open('humanbrain.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        
        # write the header row
        header = ['Gender', 'Age range', 'Head Size', 'Brain Weight']
        writer.writerow(header)
        
        # write the data rows
        for i in range(rows):
            gender = random.choice(['Male', 'Female'])
            age_range = random.randint(1,111)
            head_size = random.randint(3500, 4600)
            brain_weight = random.randint(1200, 1600)
            row = [gender, age_range, head_size, brain_weight]
            writer.writerow(row)

# generate a dataset with 237 rows and 4 columns
generate_dataset(237, 4)