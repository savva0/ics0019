#!/usr/bin/env python3

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import json

# URL to querry
# Make sure to have 'en' for English!
URL = "https://www.osta.ee/en/category/computers/"

# Upper limit for pages to querry
LIMIT = 7

def main():

    # Instantiate list to populate with data
    data = []

    # Instantiate a page count
    index = 1
    
    while(True):

        # Break out of the loop if got to the limit
        if index == LIMIT:
            break

        # Weird bug on osta where page #2 is not displayed
        # Indcrement index and skip iteration
        if index == 2:
            index += 1
            continue

        # Fetch url
        with urlopen(URL + "page-" + str(index)) as response:

            # Instantiate parser
            soup = BeautifulSoup(response, "html.parser")

            # Look for the last page
            # If got to the last page, break out of the loop
            last_page = soup.find("article", class_ = "main-article")
            
            # Class 'main-article' only exists on the last page
            # So a legit page with items will return None
            if last_page != None:

                # If page says "No products found"
                # The last page has been reached
                if last_page.get_text().lstrip().rstrip() \
                    == "No products found":
                    break

            # Loop through list of 
            for item in soup.find_all("li", class_ = "mb-30"):

                # Get "buy now" price
                price = item.find("span", class_ = "price-bn")

                # If "buy now" price is unavailable, get "current bid" price
                if price == None:
                    price = item.find("span", class_ = "price-cp")
                
                # Add data to the list
                data.append({
                    "Title": item.find("p", class_ = "offer-thumb__title").\
                        find("a").get_text(),
                    "Price": price.get_text(),
                    "Picture href": item.find("a", class_ = "lazy").\
                        find("img").get("data-original"),
                })

            # Increment index to get to the next page on next loop iteration
            index += 1

        # Save list as json
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)

if __name__ == "__main__":
    main()