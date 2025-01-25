#%

#Import dependencies
import csv
import json

#File names
csv_file_path = 'input.csv' #Replace with .csv file to convert
json_file_path = 'output.json' #Replace with .json file you want

with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = [row for row in csv_reader]


with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)
