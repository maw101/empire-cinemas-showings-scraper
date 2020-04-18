import requests
from bs4 import BeautifulSoup

# enter url for a particular Empire Cinema location (found at: https://www.empirecinemas.co.uk)
url = ""

if (url != ""): # check url not empty
    webpage = requests.get(url).text # get html content of webpage
    
    soup = BeautifulSoup(webpage, "html.parser") # create beautiful soup object
    
    filmCounter = 1
    filmsNowShowing = soup.find('div', attrs={'class': 'line-after-last-perf'}) # get array of film data in 'now showing' section
    filmList = filmsNowShowing.findAll('div', attrs={'class': 'infos'})
    
    for filmInfo in filmList:
      filmHeading = filmInfo.find('h2')
      filmTitle = filmHeading.find('a').text.strip() # get raw text for heading
      filmDescription = filmHeading.find('a')['data-content'] # get value of attribute 'data-content' from 'a' tag
      print(str(filmCounter) + ") " + filmTitle + "\n") # print out film title
      print(filmDescription + "\n") # print out film description
      filmCounter += 1
