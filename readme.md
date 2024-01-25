# Excel to JSON and JSON to Excel Converter

## Overview

This repository contains two Python scripts (`excelToJson.py` and `jsonToExcel.py`) that facilitate the conversion of data between Excel (.xlsx) and JSON formats. The scripts automate the process, making it easy to switch between these common data interchange formats.

## Features

### 1. Excel to JSON Conversion

The `excelToJson.py` script performs the following tasks:

- Reads Excel files from the specified folder (`excel` by default).
- Converts the data into a custom dictionary.
- Writes the dictionary to JSON files in the specified output folder (`json` by default).
- Supports multiple Excel files in the input folder.

### 2. JSON to Excel Conversion

The `jsonToExcel.py` script performs the reverse conversion:

- Reads JSON files from the specified folder (`json` by default).
- Converts the JSON data into a pandas DataFrame.
- Writes the DataFrame to Excel files in the specified output folder (`excel` by default).
- Supports multiple JSON files in the input folder.

## Usage

### Excel to JSON Conversion

1. Place your Excel files in the `excel` folder.
2. Run the `excelToJson.py` script.
3. JSON files will be generated in the `json` folder.

```bash
python excelToJson.py
