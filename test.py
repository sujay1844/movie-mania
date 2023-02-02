from seats import Show
from dataclasses import asdict
import json

show = Show(
    name = "Avatar",
    director = 'James Cameron',
    imdb_rating = 7.8,
    timing = '11:00PM',
    screen_no = 4,
    no_of_rows = 5,
    no_of_columns = 5,
    file_name = 'avatar.json'
)

with open('movie.json', 'w') as file:
    json.dump(asdict(show), file, indent=4)
