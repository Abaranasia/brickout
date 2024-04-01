poetry shell # to run virtual env

poetry run python main.py # to execute main app, similar to python main.py

poetry run pytest # to run tests

poetry run gunicorn -w 4 myapp:app # to serve


