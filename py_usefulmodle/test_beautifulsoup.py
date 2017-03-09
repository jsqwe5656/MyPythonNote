# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib import request

with request.urlopen('https://www.python.org/events/python-events') as page:
    soup = BeautifulSoup(page,'lxml')

count = len(soup.select('h3[class="event-title"]'))
for i in range(count):
    print('event-title:', soup.select('h3[class="event-title"]')[i].get_text())
    print('event-time:', soup.select('time')[i].get_text())
    print('event-location:', soup.select('span[class="event-location"]')[i].get_text())
    print('-' * 20)
