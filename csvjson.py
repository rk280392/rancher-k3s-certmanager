import csv
import argparse
import os
import json

def make_json(csv_file, json_file):
    data = []

    with open(csv_file, 'r', encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            data.append(rows)

    with open(json_file, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file", type=str, help="CSV file to process")
    args = parser.parse_args()

    if not os.path.isfile(args.csv_file):
        print(f"Error: The file '{args.csv_file}' does not exist.")
        exit(1)

    # Create a JSON file with the same name as the CSV file but with a .json extension
    json_file = os.path.splitext(args.csv_file)[0] + ".json"

    make_json(args.csv_file, json_file)

