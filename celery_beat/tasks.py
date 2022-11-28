from celery import shared_task
from bs4 import BeautifulSoup
import requests
from celery_beat.models import Author, Quote


@shared_task
def check_post():
    quote_l = {}
    base_url = 'https://quotes.toscrape.com'
    html_doc = requests.get(base_url)
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    quote = soup.find_all("div", {'class': 'quote'})
    for ele in quote:
        text = ele.find('span', {'class': 'text'}).string
        author = ele.find('small', {'class': 'author'}).string
        quote_l.update({text: author})
    try:
        while soup.nav.find('li', {'class': 'next'}).a['href']:
            url = base_url + soup.nav.find('li', {'class': 'next'}).a['href']
            html_doc = requests.get(url)
            soup = BeautifulSoup(html_doc.text, 'html.parser')
            quote = soup.find_all("div", {'class': 'quote'})
            for ele in quote:
                text = ele.find('span', {'class': 'text'}).string
                author = ele.find('small', {'class': 'author'}).string
                quote_l.update({text: author})
    except AttributeError:
        print('All quotes was find')
    calc = 0
    while calc < 6:
        for i in quote_l:
            if not Quote.objects.filter(text=i).exists():
                Author.objects.get_or_create(name=quote_l.get(i))
                Quote.objects.create(text=i, authors=Author.objects.get(name=quote_l.get(i)))
        calc += 1
        print(calc)



            # obj, status = Quote.objects.get_or_create(
            #     text=i,
            #     authors=quote_l.get(i)
            # )
            # if status:
            #     calc += 1
            #     Author.objects.get_or_create(
            #         name=quote_l.get(i),
            #         quotes=obj
            #     )





    # for i in soup.find_all("span", {'class': 'text'}):
    #     quote_l.append(i.string)

    # url = soup.nav.find('li', {'class': 'next'}).a['href']

    # for i in soup.find_all("span", {'class': 'text'}):
    #     obj, status = Quote.objects.get_or_create(
    #         text=i,
    #     )
    #     if status:
    #         calc += 1


    # for i in soup.find_all("span", {'class': 'text'}):
    #     print(i.string)
    #
    # for i in soup.find_all('small'):
    #     print(i.string)

    # < nav >
    # < ul
    # class ="pager" >
    # < li
    # class ="next" >
    # < a
    # href = "/page/2/" > Next < span
    # aria - hidden = "true" >→ < / span > < / a >
    # < / li >
    # < / ul >
    # < / nav >
