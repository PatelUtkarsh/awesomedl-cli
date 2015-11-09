import urllib
import re
import webbrowser

from lxml import html

def extract_download_link(link):
	start = link.find('url/') + 4
	return link[start:]

url = "http://awesomedl.ru/?" + urllib.urlencode({'s':raw_input("Please enter Show name: ")})
print url
searchpage = html.fromstring(urllib.urlopen(url).read())

epilink = searchpage.xpath("//div[@class='post-wrap']//h2//a")[0]
epilink = epilink.get("href")
#print "link ", epilink

finalstr = []
epipage = html.fromstring(urllib.urlopen(epilink).read())
for downlink in epipage.xpath("//div[@class='entry']//a"):
	if str(downlink.text).lower() == 'mega':
		finalstr.append(downlink.get("href"))
		#print "Name", downlink.text, "URL", downlink.get("href")
finallinks = [extract_download_link(dw) for dw in finalstr] 
[webbrowser.open(url,0,True) for url in finallinks]