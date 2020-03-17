import requests
import random
from bs4 import BeautifulSoup

URL = "http://quotes.toscrape.com/page/"


def makeRandomPageRequest():
    rand_num = random.randint(1, 10)
    page = requests.get(f"{URL}{rand_num}/")

    if page.status_code == 200:
        k_soup = BeautifulSoup(page.content, 'html.parser')

    else:
        print("your request was denied")
        quit()

    all_spans = k_soup.find_all('span', class_='text')

    return all_spans


def randomQuote(list_of_quotes):
    random_num = random.randint(0, 9)
    return list_of_quotes[random_num].get_text()


list_o_quotes = makeRandomPageRequest()
print(randomQuote(list_o_quotes))
