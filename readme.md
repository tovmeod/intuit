DRF project using python 3.11

After creating the virtualenv install dependencies using
`pip install -r requirements.txt`

The project is configured to use sqlite, the initial db is provided with a default user and password (avraham, secret).
To recreate the db one needs to create the tables, user and insert the initial data:

```
python manage.py migrate
python manage.py createsuperuser
python manage.py import Player.csv
```

DRF provides a browsable API, run the development server and open it with your browser:

`python manage.py runserver 8000`

http://127.0.0.1:8000/api/

The project was configured to allow anonymous access to the API, not need to login

The following will give the full list, opening it may take a few seconds and memory:

http://127.0.0.1:8000/api/players/

to open one player example:
http://127.0.0.1:8000/api/players/bohenpa01/