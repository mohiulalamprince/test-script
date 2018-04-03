import mechanize
import re

from bs4 import BeautifulSoup

br = mechanize.Browser()

br.addheaders = [('User-agent', 'Mozilla/5.0')]
br.set_handle_robots(False)

html = br.open("https://www.google.com/search?q=nestle%20merger&tbm=nws&&gws_rd=ssl")

html = html.read().lower()

soup = BeautifulSoup(html, 'html.parser')

#urls = soup.find_all("a", re.compile("l _HId"))
urls = soup.find_all("h3")

for url in urls:
    title = url.find("a").text
    print title

    url = url.find("a")['href']
    url = url[url.find('/url?q=') + 7:url.find('&sa=')]
    print url

descriptions = soup.findAll("div", {"class" : "st"})

for description in descriptions:
    print description.text
