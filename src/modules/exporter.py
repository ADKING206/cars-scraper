thonimport json
import csv

def export_data(data, file_path):
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    except Exception as e:
        raise ValueError(f"Error exporting data to {file_path}: {e}")