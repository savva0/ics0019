# Homework 2

The code in app.py does the following:

1. Creates the database
2. Adds two tables 'canteens' and 'providers'.
3. Adds TalTech canteens to the databse
4. Adds itcollege canteen to the database
5. Queries DB for canteens which are open 16.15-18.00
6. Queries DB for canteens which are serviced by Rahva Toit

On each run canteens are added to the db,
the code does not check if canteen already exists

## How o run

1. Use [pipenv](https://pipenv.pypa.io/en/latest/) to install dependencies

```sh
pipenv install
```

2. Run the app with pipenv

```sh
pipenv run python3 app.py
```