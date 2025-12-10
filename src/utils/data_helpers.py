import csv
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / 'data'

def read_users_csv(filename='users.csv'):
    path = DATA_DIR / filename
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

def read_users_json(filename='users.json'):
    path = DATA_DIR / filename
    with open(path, encoding='utf-8') as f:
        return json.load(f)
