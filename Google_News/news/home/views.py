from django.shortcuts import render, HttpResponse, redirect
from bs4 import BeautifulSoup
from urllib.request import urlopen
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout


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

        dict = {
            "images" : images,
            "title" : title,
            "story_url" : story_url,
            "brief" : brief,
            "date" : date
        }

        articles_list.append(dict)

    context={'allNews': articles_list}
    return render(request, "home.html", context )


def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be more than 10 characters")
            context={'allNews': []}
            return render(request, "home.html", context)

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            context={'allNews': []}
            return render(request, "home.html", context)
        if (pass1!= pass2):
            messages.error(request, " Passwords do not match")
            context={'allNews': []}
            return render(request, "home.html", context)
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            context={'allNews': []}
            return render(request, "home.html", context)
        else:
            messages.error(request, "Invalid credentials! Please try again")
            context={'allNews': []}
            return render(request, "home.html", context)

    return HttpResponse("404- Not found")
   

    return HttpResponse("login")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    context={'allNews': []}
    return render(request, "home.html", context)