poetry shell # to run virtual env

poetry run python main.py # to execute main app, similar to python main.py

poetry run pytest # to run tests

poetry run gunicorn -w 4 myapp:app # to serve


# Planned upgrades:

- Refactor to extract global values
- Refactor to extract object classes
- Refactor to extract helper functions
- Refactor to create different levels
- Make player score and lives persistent among levels
- Add start screen scene 
- Fix level transition scene
- Add different bricks