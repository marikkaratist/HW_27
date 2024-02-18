import csv
import json


def csv_to_json(csv_file, json_file):
    with open(csv_file, "r", encoding="utf-8") as file:
        # Создаем читателя csv
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)

    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

csv_to_json("ads.csv", "ads.json")
csv_to_json("categories.csv", "categories.json")
