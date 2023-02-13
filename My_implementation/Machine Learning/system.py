import csv
import random
import string

# List of possible values for the Instruction attribute for X86 ISA
instructions = ['mov', 'add', 'pop', 'push', 'sub', 'inc', 'dec', 'imul', 'idiv', 'and', 'or', 'xor', 'not', 'neg', 'shl', 'jmp', 'jne', 'cmp', 'call', 'ret']

# List of possible values for the Type attribute
types = ['Rtype','Itype','Stype','SBtype']

# List of possible values for the Decode attribute
decodes = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZ']

# List of possible values for the Address attribute
addresses = [None,
            random.randint(1, 100),
            random.randint(101, 200),
            random.randint(201, 300), 
            random.randint(301, 400)]

# List of possible values for the Fetched attribute
fetched = ['Y', 'N']

# Create the header for the CSV file
header = ['InstructionId', 'Leaked', 'Iclass', 'Instruction', 'Type', 'ExecTime', 'NCompo', 'DependencyN', 'Decode', 'Cost', 'Address', 'Fetched']

# Number of rows to generate
num_rows = 900

# Generate the data for the rows
data = []
for i in range(num_rows):
    data.append([i + 1, random.randint(0, 1), random.randint(0, 4), random.choice(instructions), random.choice(types), random.uniform(0, 40), random.randint(0, 4), random.randint(0, 3), random.choice(decodes), random.uniform(0, 60), random.choice(addresses), random.choice(fetched)])

# Write the data to a CSV file
with open('system.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)