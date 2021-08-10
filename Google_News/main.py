from bs4 import BeautifulSoup
from urllib.request import urlopen


def request(url):
    res = urlopen(url)
    data = res.read()
    res.close()
    soup = BeautifulSoup(data, 'lxml')            # lxml and xml diff
    return soup

urls = ['https://www.indiatoday.in/top-stories']
soup = request(urls[0])

temp = soup.find_all('div',{'class':'catagory-listing'})
articles_list = []

for news in temp:
    images = news.find('img')['src']
    title = news.find('a').text
    story_url = 'https://www.indiatoday.in'+news.find('a')['href']
    brief = news.find('p').text
    wd = ""
    for word in brief:
        if(word!='\n'):
            wd+=word
    brief = wd

    soup2 = request(story_url)
    date = soup2.find('dt',{'class':'pubdata'}).text

    articles_list.append([title, story_url, brief, images])
    
