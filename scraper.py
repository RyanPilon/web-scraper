import requests
import re
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/History_of_Mexico"

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')



def get_citations_needed_count(URL):
    
    results = soup.find_all('span', string= re.compile("citation needed"))
    return len(results)


def get_citations_needed_report(URL):

    results = soup.find_all('span', string= re.compile("citation needed"))
    results_string = "\n".join([str(tag) for tag in results])
    return results_string

print(get_citations_needed_report(URL))
print(get_citations_needed_count(URL))
