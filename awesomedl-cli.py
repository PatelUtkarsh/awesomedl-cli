import sys
import six.moves.urllib as urllib
import six
import re
import webbrowser
import xmltodict
from lxml import html


def extract_download_link(link):
    start = link.find('https')
    return link[start:]
if len(sys.argv) <= 1:
    show_name = six.moves.input("Please enter Show name: ")
else:
    show_name = sys.argv[1]
url = "http://awesomedl.ru/?" + urllib.parse.urlencode({'feed': 'rss2', 's': show_name.replace(' ','.')})
searchpage = urllib.request.urlopen(url).read()
result = xmltodict.parse(searchpage)
finalstr = []
if 'rss' in result and 'channel' in result['rss'] and 'item' in result['rss']['channel']:
    for episode in result['rss']['channel']['item']:
        epilinks = html.fromstring(episode['content:encoded'])
        links = []
        for downlink in epilinks.xpath("//a"):
            if str(downlink.text).lower() == 'mega':
                links.append(extract_download_link(downlink.get("href")));
        finalstr.append({'title': episode['title'], 'link': links})
    [webbrowser.open(url, 0, True) for url in finalstr[0]['link']]
    #print(finalstr)
else:
    print('No result found')
exit()
