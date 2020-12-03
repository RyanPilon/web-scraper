import requests
import re
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/History_of_Mexico"

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('span', string= re.compile("citation needed"))

results_string = "\n".join([str(tag) for tag in results])

get_citations_needed_count = print(len(results))

get_citations_needed_report = print(results_string)
