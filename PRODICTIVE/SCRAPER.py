import bs4
import re
import urllib2

url = "http://www.juryverdictalert.com/search-verdicts?q=car+medical&Search="
jury = "http://www.juryverdictalert.com"
import urllib2
html = urllib2.urlopen(url)

soup = bs4.BeautifulSoup(html)
[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
visible_text = soup.getText()
html = urllib2.urlopen(url)
soup = bs4.BeautifulSoup(html)

for a in soup.find_all('a', href=True):
     if str(a['href']).find("/jury-verdicts/item/") != -1:
        link =str(a['href'])

        html = urllib2.urlopen(jury+a['href'])
        soup = bs4.BeautifulSoup(html)
        [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
        linkname = 'new verdicts/'+link[(link).rfind('/')+1:]+'.txt'
        visible_text = soup.getText()
        f= open(linkname,'w')
        f.write( visible_text.encode('utf-8') )
        f.close()
