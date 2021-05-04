from django.shortcuts import render, HttpResponse

def index(request):
    # return HttpResponse("This is Homepage")
    context = {
        'variable' : "This is a variable"
    }
    return render(request, 'index.html',context)

def about(request):
    return HttpResponse("This is About Us page")