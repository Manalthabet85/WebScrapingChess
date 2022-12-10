from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas

'''driver = webdriver.Chrome()
driver.get("https://lichess.org/@/Manal_Th3/bookmark")'''
driver = requests.get('https://lichess.org/@/Manal_Th3/bookmark')
chessFormat = []
matchDate = []
whitePlayerName = []
whitePlayerRate = []
blackPlayerName = []
blackPlayerRate = []
results = []
openings = []

content = driver.content
soup = BeautifulSoup(content, 'html.parser')
bio = soup.find('p', attrs={'class':'bio'})
print(bio.text)
for tag in soup.findAll('div', attrs={'class':'game-row__infos'}):
    chFormat = tag.find('strong')
    date = tag.find('time')
    white = tag.find('div', attrs={'class':'player white'})
    wName = white.find('a', attrs={'class':'user-link'})
    wRate = white.contents[2]
    black = tag.find('div', attrs={'class':'player black'})
    bName = black.find('a', attrs={'class':'user-link'})
    bRate = black.contents[2]

    result = tag.find('div', attrs={'class':'result'})
    opening = tag.find('div', attrs={'class':'opening'})

    chessFormat.append(chFormat.text.replace('•', '-'))
    if 'title' in date.attrs:
        matchDate.append(date.attrs['title'])
    else:
        matchDate.append(date.text)
    whitePlayerName.append(wName.text)
    whitePlayerRate.append(wRate.text)
    blackPlayerName.append(bName.text)
    blackPlayerRate.append(bRate.text)
    results.append(result.text.replace('•', '-'))
    openings.append(opening.next_element.text)

print(chessFormat)
print(matchDate)
print(whitePlayerName)
print(whitePlayerRate)
print(blackPlayerName)
print(blackPlayerRate)
print(results)
print(openings)


df = pandas.DataFrame({'Chess Game Format': chessFormat, 'Match Date': matchDate, 'White Player Name': whitePlayerName, 'White Player Rate': whitePlayerRate, 'Black Player Name': blackPlayerName, 'Black Player Rate': blackPlayerRate, 'Results': results, 'Openings': openings})
df.to_csv('MyChessMatches.csv', index=False, encoding='utf-8')



