#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The following code creates a new database and populates it with data
in accordence with the task
"""

from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker, query
from sqlalchemy import types
from datetime import time

# Create DB connection, use "sqlite:///" to store db in memory
# Set echo to True for verbose output
engine = create_engine("sqlite:///diners.db", echo = False)

Base = declarative_base()

# Define class for Canteens
class Canteen(Base):
    __tablename__ = "canteens"

    id = Column(Integer, primary_key = True, unique=True)
    name = Column(String)
    location = Column(String)
    time_open = Column(types.Time)
    time_closed = Column(types.Time)

    provider_id = Column(Integer, ForeignKey("providers.id"))

    provider = relation("Provider", backref="canteens", lazy=True)

    def __init__(self, name = None, location = None, time_open = None, 
        time_closed = None, provider_name = None):
        self.name = name
        self.location = location
        self.time_open = time_open
        self.time_closed = time_closed

        # Check if provider already exists
        p = session.query(Provider).filter_by(name = provider_name).first()
        # If yes, reuse
        if p:
            self.provider = p
        # If no, create a new instance
        else:
            self.provider = Provider(name = provider_name)

# Define class for Providers
class Provider(Base):
    __tablename__ = "providers"

    id = Column(Integer, primary_key = True, unique=True)
    name = Column(String, nullable=False, unique=True)

    def __init_(self, name = None):
        self.name = name

# Create DB
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind = engine)
session = Session()

# Declare TalTech canteen list
ttu_canteens = [
    {
        "Name": "Economics and social science building canteen",
        "Location": "Akadeemia tee 3 SOC building",
        "ProviderName": "Rahva Toit",
        "time_open": "8:30",
        "time_closed": "18:30"
    },

    {
        "Name": "Libary canteen",
        "Location": "Akadeemia tee 1/Ehitajate tee 7",
        "ProviderName": "Rahva Toit",
        "time_open": "8:30",
        "time_closed": "19:00"
    },

    {   
        "Name": "Main building Deli cafe",
        "Location": "Ehitajate tee 5 U01 building",
        "ProviderName": "Baltic Restaurants Estonia AS",
        "time_open": "9:00",
        "time_closed": "16:30"
    },

    {
        "Name": "Main building Daily lunch restaurant",
        "Location": "Ehitajate tee 5 U01 building",
        "ProviderName": "Baltic Restaurants Estonia AS",
        "time_open": "9:00",
        "time_closed": "16:30"
    },

    {
        "Name": "U06 building canteen",
        "Location": "Ehitajate tee 5 U06 building",
        "ProviderName": "Rahva Toit",
        "time_open": "9:00",
        "time_closed": "16:00"
    },

    {
        "Name": "Natural Science building canteen",
        "Location": "Akadeemia tee 15 SCI building",
        "ProviderName": "Baltic Restaurants Estonia AS",
        "time_open": "9:00",
        "time_closed": "16:00"
    },

    {
        "Name": "ICT building canteen",
        "Location": "Raja 15/Mäepealse 1",
        "ProviderName": "Baltic Restaurants Estonia AS",
        "time_open": "9:00",
        "time_closed": "16:00"
    },

    {
        "Name": "Sports building canteen",
        "Location": "Männiliiva 7 S01 building",
        "ProviderName": "TTÜ Sport OÜ",
        "time_open": "11:00",
        "time_closed": "20:00"
    }
]

# Add TalTech canteen list to DB
for canteen in ttu_canteens:
    c = Canteen(canteen["Name"], canteen["Location"],
                time(hour = int(canteen["time_open"].split(":")[0]),
                        minute = int(canteen["time_open"].split(":")[1])),
                time(hour = int(canteen["time_closed"].split(":")[0]),
                        minute = int(canteen["time_closed"].split(":")[1])),
                provider_name = canteen["ProviderName"])
    session.add(c)
session.commit()

# Declare itcollege canteen dict
itcollege_canteen = {
    "Name": "bitStop KOHVIK",
    "Location": "Raja 4",
    "ProviderName": "Bitstop Kohvik OÜ",
    "time_open": "9:30",
    "time_closed": "16:00"
}

# Add itcollege canteen dict to DB
c = Canteen(itcollege_canteen["Name"], itcollege_canteen["Location"],
    time(hour = int(itcollege_canteen["time_open"].split(":")[0]),
            minute = int(itcollege_canteen["time_open"].split(":")[1])),
    time(hour = int(itcollege_canteen["time_closed"].split(":")[0]),
            minute = int(itcollege_canteen["time_closed"].split(":")[1])),
    provider_name = itcollege_canteen["ProviderName"])
session.add(c)
session.commit()

# Query DB for all canteens open between 16:15 and 18:00
# and print to the screen
print("Query DB for all canteens open between 16:15 and 18:00")
for item in session.query(Canteen, Provider).\
    filter(Canteen.provider_id == Provider.id).\
    filter(Canteen.time_open <= time(hour = 16, minute = 15)).\
    filter(Canteen.time_closed >= time(hour = 18, minute = 00)).all():
    print("Name: ", item.Canteen.name, "Location: ", item.Canteen.location, 
    "Provider: ", item.Provider.name, "Open: ",item.Canteen.time_open,
    "Closed: ", item.Canteen.time_closed)

# Query DB for all canteens serviced Rahva Toit
# and print to the screen
print("Query DB for all canteens serviced Rahva Toit")
for item in session.query(Canteen, Provider).\
    filter(Canteen.provider_id == Provider.id).\
    filter(Provider.name == "Rahva Toit").all():
    print("Name: ", item.Canteen.name, "Location: ", item.Canteen.location, 
    "Provider: ", item.Provider.name, "Open: ", item.Canteen.time_open,
    "Closed: ", item.Canteen.time_closed)
