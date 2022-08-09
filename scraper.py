import re
import requests
from bs4 import BeautifulSoup


#Define url and get page content

url = 'https://en.wikipedia.org/wiki/Cyberwarfare'


#first element with a given class



citations= []



def get_citations_needed_count(url='https://en.wikipedia.org/wiki/Cyberwarfare'):
  #Loop through the resulting p tags and extract 

  citations_count = 0
  
  page = requests.get(url)

  #Use the Beautiful soup
  soup =BeautifulSoup(page.content, "html.parser")
  results = soup.find_all('p')
  page = soup()
  #print(soup)

  for element in results:
    text = str(element.text)


  # Get the number of citations
    for child in element.children:
      if "Citation needed" in str(element):
                paragraph = element.text.split('[citation')[0]
                print(paragraph)
                citations_count = citations_count + 1
                break

  #


def get_citations_needed_report(url='https://en.wikipedia.org/wiki/Cyberwarfare'):
  #Loop through the resulting p tags and extract 

  citations= []
  report_string = ""
  
  page = requests.get(url)

  #Use the Beautiful soup
  soup =BeautifulSoup(page.content, "html.parser")
  results = soup.find_all('p')
  page = soup()
  #print(soup)

  for element in results:
    text = str(element.text)


  # Get the number of citations
    for child in element.children:
      if "Citation needed" in str(element):
                paragraph = element.text.split('[citation')[0]
      
                report_string = report_string + f'\n > {paragraph}'
                

                break

  print(report_string)            
  return report_string


#Uncomment the line below to test function(s)
#get_citations_needed_count(url)

#get_citations_needed_report(url)
