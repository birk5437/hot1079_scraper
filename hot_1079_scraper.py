import urllib2
from BeautifulSoup import BeautifulSoup
import time
import csv
import re

#csv stuff not used yet
#csvwriter = csv.writer(open('macbookall3.csv', 'w'), delimiter=',')

def re2num(rexp,isint,searchspace):
	if isint:
		num=re.search(rexp,searchspace)
		try:
			num=re.search('[0-9]+',num.group(0))
			return int(num.group(0))
		except:
			return ''
	else:
		num=re.search(rexp,searchspace)
		try:
			num=re.search('\d+\.\d+',num.group(0))
			return float(num.group(0))
		except:
			return ''

def getnum(rexp,isint,searchspaces,val,n):
	if val=='':
		if n<2:
			val=re2num(rexp,isint,searchspaces[n])
		else:
			val='NotFound'
		return getnum(rexp,isint,searchspaces,val,n+1)
	else:
		return val

#get file here and save-as with chrome (i need to get wget to run the javascript):
#http://r2b.yes.com/chat-previd/litechat.php?station=WHTA&style=red&slogan=Hot+107.9+Atlanta%26apos%3Bs+Real+Hip-Hop+and+R%26amp%3BB+Station
http='file:///Users/burke/programming_stuff/python/hot1079_scraper/Chat_Lite.html'
#print http
request = urllib2.urlopen(http)
html = request.read()
soup=BeautifulSoup(html)
#print html
#for q in soup.findAll("span"):
art = ""
tit = ""
rnk = ""
for q in soup.findAll(attrs={'class' : "undefined"}):
	soup2 = BeautifulSoup(str(q))
	for info in soup2.findAll(attrs={'class' : "liteInfo"}):
		soup3 = BeautifulSoup(str(info))
		for artist in soup3.findAll(attrs={'class' : "liteRecord"}):
			#print artist.contents
			art = artist.contents
			
		for title in soup3.findAll(attrs={'class' : "liteTitle"}):
			tit = title.contents[0].contents

		for rank in soup2.findAll(attrs={'class' : "liteRank"}):
			#print rank.contents[2].contents
			rnk = rank.contents[2].contents
			#print title.contents[0].contents
		print (str(art) + ", " + str(tit) + ", " + str(rnk)).replace("[u'", "").replace("']", "").replace("[u\"","").replace("\"]","")
	#link = q.contents[0].contents[0]
	#print link
		
