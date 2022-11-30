from celery import shared_task
from bs4 import BeautifulSoup
import requests
from celery_beat.models import Author, Quote
from django.core.mail import send_mail


@shared_task
def check_post():
    quote_l = []
    base_url = 'https://quotes.toscrape.com'
    html_doc = requests.get(base_url)
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    quote = soup.find_all("div", {'class': 'quote'})
    for ele in quote:
        text = ele.find('span', {'class': 'text'}).string
        author = ele.find('small', {'class': 'author'}).string
        if not Quote.objects.filter(text=text).exists():
            quote_l.append({text: author})
    try:
        while soup.nav.find('li', {'class': 'next'}).a['href']:
            url = base_url + soup.nav.find('li', {'class': 'next'}).a['href']
            html_doc = requests.get(url)
            soup = BeautifulSoup(html_doc.text, 'html.parser')
            quote = soup.find_all("div", {'class': 'quote'})
            for ele in quote:
                text_1 = ele.find('span', {'class': 'text'}).string
                author = ele.find('small', {'class': 'author'}).string
                if not Quote.objects.filter(text=text_1).exists():
                    quote_l.append({text_1: author})
    except AttributeError:
        if len(quote_l) == 0:
            send_mail('check_post_results', 'No one new quotes was find', 'no_reply@somecompany.com',
                      ['admin_email@somecompany.com'])
        else:
            for e in quote_l[:5]:
                for a in e:
                    Author.objects.get_or_create(name=e[a])
                    Quote.objects.create(text=a, authors=Author.objects.get(name=e[a]))
