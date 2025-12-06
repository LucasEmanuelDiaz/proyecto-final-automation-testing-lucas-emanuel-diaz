import json
import csv
import os

class DataLoader:
    @staticmethod
    def load_json(path: str):
        full = os.path.join(os.getcwd(), path)
        with open(full, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def load_csv(path: str):
        full = os.path.join(os.getcwd(), path)
        rows = []
        with open(full, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for r in reader:
                rows.append(r)
        return rows
