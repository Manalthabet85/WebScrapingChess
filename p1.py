import requests
import bs4
url ='https://realpython.github.io/fake-jobs'
page = requests.get(url)
#print(page.content)
soup = bs4.BeautifulSoup(page.content,"html.parser")
print(soup.find('h1',{'class':'title is-1'}))
