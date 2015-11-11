import urllib
import re
import webbrowser
import xmltodict

from lxml import html

def extract_download_link(link):
	start = link.find('url/') + 4
	return link[start:]

url = "http://awesomedl.ru/?" + urllib.urlencode({'feed':'rss2','s':raw_input("Please enter Show name: ")})
searchpage = urllib.urlopen(url).read()
result = xmltodict.parse(searchpage)
finalstr = []
if result.has_key('rss') and result['rss'].has_key('channel') and result['rss']['channel'].has_key('item'):
	for episode in result['rss']['channel']['item']:
		epilinks = html.fromstring(episode['content:encoded'])
		links = []
		for downlink in epilinks.xpath("//a"):
			if str(downlink.text).lower() == 'mega':
				links.append(extract_download_link(downlink.get("href")));
		finalstr.append({'title':episode['title'], 'link':links})
	[webbrowser.open(url,0,True) for url in finalstr[0]['link']]
	print finalstr
else:
	print 'no result found'
exit();