import json
from json.decoder import JSONDecodeError
import os
from dataclasses import dataclass, asdict

@dataclass
class Show:
    name: str
    director: str
    imdb_rating: float
    timing: str

    screen_no: int
    no_of_rows: int
    no_of_columns: int

    file_name: str


def create_show(show:Show):
    try:
        with open('shows.json', 'r') as file:
                shows = json.load(file)

    except (JSONDecodeError, FileNotFoundError):
        # First time use
        with open('shows.json', 'w') as file:
            file.write('[]')
        shows = []

    # Avoid duplicates
    if asdict(show) in shows: return

    shows.append(asdict(show))
    with open('shows.json', 'w') as file:
        json.dump(shows, file)

