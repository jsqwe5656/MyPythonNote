# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.valid_title = False
        self.valid_date = False
        self.valid_location = False
        self.valid_year = False
        self.information = []

    def handle_starttag(self, tag, attrs):
        print(tag,len(attrs))
        if tag == 'h3' and len(attrs) != 0 and attrs[0][1] == 'event-title':
            self.valid_title = True
        elif tag == 'time' and len(attrs) != 0 and attrs[0][0] == 'datetime':
            self.valid_date = True
        elif tag == 'span' and len(attrs) != 0 and attrs[0][1] == 'say-no-more':
            self.valid_year = True
        elif tag == 'span' and len(attrs) != 0 and attrs[0][1] == 'event-location':
            self.valid_location = True

    def handle_endtag(self, tag):
        #print('</%s>' % tag)
        pass

    def handle_startendtag(self, tag, attrs):
        #print('<%s/>' % tag)
        pass

    def handle_data(self, data):
        #print(data)
        if self.valid_title == True:
            self.information.append([])
            self.information[-1].append(data)
            self.valid_title = False
        elif self.valid_date == True:
            self.information[-1].append([data])
            self.valid_date = False
        elif self.valid_year == True:
            self.information[-1][1].append(data)
            self.valid_year = False
        elif self.valid_location == True:
            self.information[-1].append(data)
            self.valid_location = False


    def handle_comment(self, data):
        #print('<!--',data,'-->')
        pass

    def handle_entityref(self, name):
       # print('&%s:' %name)
        c = chr(name2codepoint[name])
        print('name ent:')

    def handle_charref(self, name):
        #print('&#%s;' % name)
        pass

parser = MyHTMLParser()
page = request.urlopen('https://www.python.org/events/python-events/').read().decode()
parser.feed(page)