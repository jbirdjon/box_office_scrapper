# scrape.py

import os # standard imput stuff
import requests #

from bs4 import BeautifulSoup # also known as 'beautifulscraper'
from apscheduler.schedulers.blocking import BlockingScheduler # scheduler
from datetime import datetime # this will let us access current time
sched = BlockingScheduler();

def main():
    # vv enter in your phone number here vv
    phoneNumber = 1234567890
    # return list to append values in message to
    ret = []
    # get url for the page somehow here. use datetime to calculate the week
    year = datetime.now().year
    weekNum = datetime.now().isocalendar()[1]
    weekNum = weekNum - 1 # gets previous week
    url = 'https://www.boxofficemojo.com/weekend/' + str(year) + 'W' + str(weekNum) +'/?sortDir=asc&sort=rank&ref_=bo_we__resort#table'

    # initializes the beautifulsoup
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    
    for x in range(5): # this loops through each attribute in the top 5 values.
        rank = soup.find_all("td", class_="a-text-right mojo-header-column mojo-truncate mojo-field-type-rank mojo-sort-column")[x].get_text() # get the rank for the week
        title = soup.find_all("td", class_="a-text-left mojo-field-type-release mojo-cell-wide")[x].get_text() # get the title of the film
        gross = soup.find_all("td", class_="a-text-right mojo-field-type-money mojo-estimatable")[(3*x)].get_text() # get gross for the weekend
        total_gross = soup.find_all("td", class_="a-text-right mojo-field-type-money mojo-estimatable")[(x*3)+2].get_text() # get total gross
        weeks = soup.find_all("td", class_="a-text-right mojo-field-type-positive_integer")[(x*2)+1].get_text() # get number of weeks it's been in studio

        # appends values to return value
        if int(weeks) == 1:
            ret.append(rank + ": " + str(title) + " made " + str(gross) + " dollars in its opening weekend.")
        else:
            ret.append(rank + ": " + str(title) + " made " + str(gross) + " dollars last week. It has made " + str(total_gross) + " dollars over " + str(weeks) + " weeks")
        ret.append("\n")

    # joins all the values into a string that it then prints
    message = ''.join(ret)
    cmd = "osascript sendMessage.scpt " + str(phoneNumber) + " '" + str(message) + "' "
    os.system(cmd)

if __name__ == "__main__":
    main()

