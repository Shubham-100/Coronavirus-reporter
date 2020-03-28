import requests
import html5lib
import time
from bs4 import BeautifulSoup
from decimal import Decimal


# Http request to worldometer
def getcases():
    url = "https://www.worldometers.info/coronavirus/country/india/"
    req = requests.get(url)

    soup = BeautifulSoup(req.text, "html5lib")

    corona = soup.findAll('div', attrs = {'id':'maincounter-wrap'})

    cases = corona[0].find('span').text
    deaths = corona[1].find('span').text
    recovered = corona[2].find('span').text
    mortality = int(deaths)*100/int(cases)
    mortality = round(Decimal(mortality), 2)

    print("Cases: " + cases)
    print("Deaths: " + deaths)
    print("Recovered: " + recovered)
    print("Mortality rate: " + str(mortality) + "%")

while True:
    getcases()
    time.sleep(900)