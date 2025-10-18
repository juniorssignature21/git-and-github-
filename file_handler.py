import csv

def read_csv_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

data = read_csv_file("./product_mgt.csv")

for row in data:
    # print(' '.join(row[1]))
    print(row)

