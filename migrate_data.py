import os
import django

# Установите переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HW_27.settings')

# Загрузите настройки Django
django.setup()

import json

from ads.models import Ad, Category


def migrate_ads_from_json_to_sqlite(json_file):
    with open(json_file, 'r', encoding="utf-8") as f:
        data = json.load(f)

        for row in data:
            is_published = True if row["is_published"].lower() == "true" else False
            model_instance = Ad(
                Id=row["Id"],
                name=row["name"],
                author=row["author"],
                price=row["price"],
                description=row["description"],
                address=row["address"],
                is_published=is_published,
            )

            model_instance.save()


def migrate_cat_from_json_to_sqlite(json_file):
    with open(json_file, 'r', encoding="utf-8") as f:
        data = json.load(f)

        for row in data:
            model_instance = Category(
                id=row["id"],
                name=row["name"],
            )

            model_instance.save()


migrate_ads_from_json_to_sqlite("ads.json")
migrate_cat_from_json_to_sqlite("categories.json")
