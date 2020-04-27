#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def main():
    # Import data
    direct_flights = pd.read_csv("data/otselennud.csv", sep = ";")
    airports = pd.read_csv("data/airports.dat", sep = ",")

    # Merge dataframes on common column "IATA"
    # and discard all rows that are not common
    data = pd.merge(direct_flights, airports, on = "IATA")

    # Create canvas to draw
    fig = plt.figure(figsize = (10, 8))
    ax = fig.add_subplot(1, 1, 1, projection = ccrs.PlateCarree())

    # Add map features
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle = ":")
    ax.add_feature(cfeature.LAKES, alpha = 0.5)
    ax.add_feature(cfeature.RIVERS)

    # Loop through data and create a plot
    # I know that iterating through a dataframe is an antipattern
    # This is proper way to plot markers
    # but I have no idea how to plot lines and text
    # plt.plot(data["Longitude"], data["Latitude"], "bo", 
    #     transform=ccrs.Geodetic())

    TLL_data = data.loc[data["IATA"] == "TLL"]
    for index, row in data.iterrows():
        plt.plot([TLL_data["Longitude"], row["Longitude"]],
            [TLL_data["Latitude"], row["Latitude"]], color="blue",
            linewidth=2, marker="o", transform=ccrs.Geodetic())

        plt.text(row["Longitude"], row["Latitude"], row["IATA"],
            horizontalalignment="right", transform=ccrs.Geodetic())

    # Create title and set color to blue
    ax.set_title("Tallinna Lennujaama lennud 2020", {"color": "blue"})

    # Set focus to Europe
    ax.set_extent([-10, 45, 32, 70])

    # Save the plot
    plt.savefig("map.png")

    # Draw the plot
    plt.show()

if __name__ == "__main__":
    main()