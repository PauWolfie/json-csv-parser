import os
import pandas as pd
import json

# Name of the folder containing the JSON files
json_folder = 'json'

# Name of the folder where the CSV files will be saved
csv_folder = 'excel'

# Ensure that the output folder exists
if not os.path.exists(csv_folder):
    os.makedirs(csv_folder)

# Iterate over the files in the 'json' folder
for json_file_name in os.listdir(json_folder):
    if json_file_name.endswith('.json'):
        json_file_path = os.path.join(json_folder, json_file_name)

        # Read the JSON file with utf-8 encoding
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        # Create a pandas DataFrame with a default index
        df = pd.DataFrame(data.items(), columns=['Key', 'Value'])
        
        # Build the path for the output Excel file in the 'csv' folder
        csv_file_path = os.path.join(csv_folder, os.path.splitext(json_file_name)[0] + '.xlsx')

        # Write the DataFrame to an Excel file
        df.to_excel(csv_file_path, index=False)

print("JSON to Excel conversion has been completed.")
