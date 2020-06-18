import urllib.request
import bs4 as BeautifulSoup

def get_data(url):
    page=urllib.request.urlopen(url)
    source=BeautifulSoup(page.read(),"html.parser")

    #for meta data
  
    #for link
    links=[]
    for tags in html.find_all('script'):
        links.append(tags.get('src'))
    
     #str.find
    #for title
    title=source.title.text

    


