from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen

def request(url):
    res = urlopen(url)
    data = res.read()
    res.close()
    soup = BeautifulSoup(data, 'lxml')            # lxml and xml diff
    return soup


# Create your views here.
def home(request): 
    context={'allNews': []}
    return render(request, "home.html", context)

def displayNews(request):

    urls = ['https://www.indiatoday.in/top-stories']
    res = urlopen(urls[0])
    data = res.read()
    res.close()
    soup = BeautifulSoup(data, 'lxml')
    # soup = request(urls[0])

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

        res = urlopen(story_url)
        data = res.read()
        res.close()
        soup2 = BeautifulSoup(data, 'lxml')
            
        date = soup2.find('dt',{'class':'pubdata'}).text

        articles_list.append([title, story_url, brief, images])

    print("done")
    context={'allNews': articles_list}
    return render(request, "home.html",context )