import pandas as pd
import sys, os, django
from pathlib import Path
from glob import glob
import pytz

sys.path.append(str(Path(__file__).parents[1]))
os.environ["DJANGO_SETTINGS_MODULE"] = "glucosetracker.settings"
django.setup()

from api.models import GlucoseReading


def from_csv(file_path: str) -> pd.DataFrame:
    glucose_levels = pd.read_csv(
        file_path,
        skiprows=0,
        skip_blank_lines=True,
        header=1,
        parse_dates=["Gerätezeitstempel"],
    )
    glucose_levels["user id"] = file_path[9:-4]
    glucose_levels = glucose_levels[
        [
            "user id",
            "Gerät",
            "Seriennummer",
            "Gerätezeitstempel",
            "Aufzeichnungstyp",
            "Glukosewert-Verlauf mg/dL",
        ]
    ]
    headers = {
        "Gerät": "device_name",
        "Seriennummer": "device_serial",
        "Gerätezeitstempel": "timestamp",
        "Aufzeichnungstyp": "recording_type",
        "Glukosewert-Verlauf mg/dL": "glucose_level",
    }
    glucose_levels.rename(columns=headers, inplace=True)
    glucose_levels["timestamp"].dt.tz_localize("UTC").dt.tz_convert("Europe/London")
    glucose_levels["recording_type"].fillna(-1, inplace=True)
    glucose_levels["glucose_level"].fillna(-1, inplace=True)
    return glucose_levels.rename(columns=headers)


def upload_glucose_readings(path):
    data = from_csv(path)
    readings = [
        GlucoseReading(
            user_id=row["user id"],
            device_name=row["device_name"],
            device_serial=row["device_serial"],
            timestamp=pytz.utc.localize(row["timestamp"]),
            recording_type=row["recording_type"],
            glucose_level=row["glucose_level"],
        )
        for i, row in data.iterrows()
    ]
    GlucoseReading.objects.bulk_create(readings)


if __name__ == "__main__":
    for file in glob(os.path.join("api/data", "*.csv")):
        upload_glucose_readings(file)
        print(f'Upload of {file[9:]} successful.')
