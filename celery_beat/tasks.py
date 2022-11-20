from celery import shared_task
from bs4 import BeautifulSoup
import requests


@shared_task
def check_post():
    url = 'https://quotes.toscrape.com/'
    html_doc = requests.get(url)
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    for i in soup.find_all("span", {'class': 'text'}):
        print(i.string)


