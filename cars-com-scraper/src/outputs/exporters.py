thonimport json
import csv

class Exporter:
    @staticmethod
    def export_to_json(data, filename='output.json'):
        with open(filename, 'w') as outfile:
            json.dump(data, outfile, indent=4)

    @staticmethod
    def export_to_csv(data, filename='output.csv'):
        if data:
            keys = data[0].keys()
            with open(filename, 'w', newline='') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)

    @staticmethod
    def export_to_excel(data, filename='output.xlsx'):
        import pandas as pd
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)