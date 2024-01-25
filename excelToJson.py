import os
import pandas as pd
import json

# Name of the folder containing the Excel files
csv_folder = 'excel'

# Name of the folder where the JSON files will be saved
json_folder = 'json'

# Ensure that the output folder exists
if not os.path.exists(json_folder):
    os.makedirs(json_folder)

# Iterate over the files in the 'csv' folder
for csv_file in os.listdir(csv_folder):
    if csv_file.endswith('.xlsx'):
        csv_path = os.path.join(csv_folder, csv_file)

        # Read the Excel file
        df = pd.read_excel(csv_path)

        # Convert the DataFrame to a custom dictionary
        data_dict = dict(zip(df['Key'], df['Value']))

        # Build the path for the output JSON file in the 'json' folder
        json_path = os.path.join(json_folder, os.path.splitext(csv_file)[0] + '.json')

        # Write the dictionary to a JSON file
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data_dict, json_file, indent=2, ensure_ascii=False)

print("Excel to JSON conversion has been completed.")
