# Create your views here.
from app.models import *
from django.shortcuts import render,redirect
from django.http  import HttpResponse
import feedparser
 
# Create your views here.
def updatepython(request):
    #-------python----------------
    url = feedparser.parse(
            "https://medium.com/feed/tag/python"
        )
    for i in range(10):
        info = url.entries[i]
        content= PyContent()
        content.headline= info.title
        #-----finding image link
        desc = info.description
        start=desc.find("img src=")
        end=desc.find("width")
        
        print(desc[end:])
        desc=desc[start+9:end-2:]
        print("-----------------------------")
        print(desc)
 
        #---------------
        content.img = desc
        content.url  = info.link
        content.save()
    
    return redirect('/')
 
def updatecovid(request):
    #-------python----------------
    url = feedparser.parse(
            "https://medium.com/feed/tag/covid"
        )
    for i in range(10):
        info = url.entries[i]
        content= CovidContent()
        content.headline= info.title
        print("################################")
        print(content.headline)
        #-----finding image link
        desc = info.description
        start=desc.find("img src=")
        end=desc.find("width")
        
        print(desc[end:])
        desc=desc[start+9:end-2:]
        print("-----------------------------")
        print(desc)
 
        #---------------
        content.img = desc
        content.url  = info.link
        content.save()
    
    return redirect('/')
 
def updateprog(request):
    #-------python----------------
    url = feedparser.parse(
            "https://medium.com/feed/tag/programming"
        )
    for i in range(10):
        info = url.entries[i]
        content= ProgContent()
        content.headline= info.title
        #-----finding image link
        desc = info.description
        start=desc.find("img src=")
        end=desc.find("width")
        
        print(desc[end:])
        desc=desc[start+9:end-2:]
        print("-----------------------------")
        print(desc)
 
        #---------------
        content.img = desc
        content.url  = info.link
        content.save()
    
    return redirect('/')
 
def updatehiring(request):
    #-------python----------------
    url = feedparser.parse(
            "https://medium.com/feed/tag/hiring"
        )
    for i in range(10):
        info = url.entries[i]
        content= HiringContent()
        content.headline= info.title
        #-----finding image link
        desc = info.description
        start=desc.find("img src=")
        end=desc.find("width")
        
        print(desc[end:])
        desc=desc[start+9:end-2:]
        print("-----------------------------")
        print(desc)
 
        #---------------
        content.img = desc
        content.url  = info.link
        content.save()
    
    return redirect('/')
 
def home(request):
    pycontent = PyContent.objects.all()
    progcontent = ProgContent.objects.all()
    hiringcontent = HiringContent.objects.all()
    covidcontent = CovidContent.objects.all()
    context = { 
        'pycontent': pycontent,
        'progcontent': progcontent,
        'hiringcontent': hiringcontent,
        'covidcontent': covidcontent,
    }
    return render(request,'app/home.html',context)