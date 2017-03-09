# -*- coding: utf-8 -*-

'关于sax 解析xml的demo'
import requests
from xml.parsers.expat import ParserCreate
import pprint

class WeatherSaxHandler(object):
    def __init__(self):
        self.weather_data = {}

    def start_element(self, name, attributtes):
        if name == 'yweather:location':
            self.weather_data['city'] = attributtes['city']
            self.weather_data['country'] = attributtes['country']
        if name == 'yweather:forecast':
            if attributtes['day'] == 'Wed':
                self.weather_data['today'] = {'low' : int(attributtes['low']), 'high' : int(attributtes['high']), 'text' : attributtes['text']}
            if attributtes['day'] == 'Thu':
                self.weather_data['tomorrow'] = {'low' : int(attributtes['low']), 'high' : int(attributtes['high']), 'text' : attributtes['text']}

def parse_weather(xml):
    weather_handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = weather_handler.start_element
    parser.Parse(xml)
    return weather_handler.weather_data
data = r'''<query xmlns:yahoo="http://www.yahooapis.com/v1/base.rng" yahoo:count="1" yahoo:created="2016-11-07T22:18:37Z" yahoo:lang="en-US">
<results>
<channel>
<yweather:units xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" distance="km" pressure="mb" speed="km/h" temperature="C"/>
<title>Yahoo! Weather - Glasgow, Scotland, GB</title>
<link>
http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-21125/
</link>
<description>Yahoo! Weather for Glasgow, Scotland, GB</description>
<language>en-us</language>
<lastBuildDate>Mon, 07 Nov 2016 10:18 PM GMT</lastBuildDate>
<ttl>60</ttl>
<yweather:location xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" city="Glasgow" country="United Kingdom" region=" Scotland"/>
<yweather:wind xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" chill="37" direction="270" speed="6.44"/>
<yweather:atmosphere xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" humidity="71" pressure="34067.08" rising="0" visibility="25.91"/>
<yweather:astronomy xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" sunrise="7:38 am" sunset="4:23 pm"/>
<image>
<title>Yahoo! Weather</title>
<width>142</width>
<height>18</height>
<link>http://weather.yahoo.com</link>
<url>
http://l.yimg.com/a/i/brand/purplelogo//uh/us/news-wea.gif
</url>
</image>
<item>
<title>
Conditions for Glasgow, Scotland, GB at 09:00 PM GMT
</title>
<geo:lat xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">55.854099</geo:lat>
<geo:long xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">-4.2648</geo:long>
<link>
http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-21125/
</link>
<pubDate>Mon, 07 Nov 2016 09:00 PM GMT</pubDate>
<yweather:condition xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="29" date="Mon, 07 Nov 2016 09:00 PM GMT" temp="3" text="Partly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="07 Nov 2016" day="Mon" high="6" low="1" text="Partly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="5" date="08 Nov 2016" day="Tue" high="5" low="0" text="Rain And Snow"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="39" date="09 Nov 2016" day="Wed" high="7" low="1" text="Scattered Showers"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="10 Nov 2016" day="Thu" high="8" low="4" text="Partly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="12" date="11 Nov 2016" day="Fri" high="8" low="3" text="Rain"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="28" date="12 Nov 2016" day="Sat" high="8" low="6" text="Mostly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="28" date="13 Nov 2016" day="Sun" high="10" low="3" text="Mostly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="28" date="14 Nov 2016" day="Mon" high="9" low="6" text="Mostly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="28" date="15 Nov 2016" day="Tue" high="10" low="6" text="Mostly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="28" date="16 Nov 2016" day="Wed" high="8" low="6" text="Mostly Cloudy"/>
<description>
<![CDATA[<img src="http://l.yimg.com/a/i/us/we/52/29.gif"/> <BR /> <b>Current Conditions:</b> <BR />Partly Cloudy <BR /> <BR /> <b>Forecast:</b> <BR /> Mon - Partly Cloudy. High: 6Low: 1 <BR /> Tue - Rain And Snow. High: 5Low: 0 <BR /> Wed - Scattered Showers. High: 7Low: 1 <BR /> Thu - Partly Cloudy. High: 8Low: 4 <BR /> Fri - Rain. High: 8Low: 3 <BR /> <BR /> <a href="http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-21125/">Full Forecast at Yahoo! Weather</a> <BR /> <BR /> (provided by <a href="http://www.weather.com" >The Weather Channel</a>) <BR /> ]]>
</description>
<guid isPermaLink="false"/>
</item>
</channel>
</results>
</query>'''

if __name__ == '__main__':
    weather = parse_weather(data)
    print(weather)
#print(weather)
