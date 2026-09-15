import csv
import json


def csv_to_json(csv_file, json_file):
    data = []

    # Read CSV file
    with open(csv_file, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        # Convert each row into a dictionary
        for row in reader:
            data.append(row)

    # Write data to JSON file
    with open(json_file, "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, indent=4)

    print("CSV file successfully converted to JSON!")


# File names
csv_file = "input.csv"
json_file = "output.json"

# Convert CSV to JSON
csv_to_json(csv_file, json_file)
