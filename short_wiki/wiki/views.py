# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4
from .forms import SearchForm
import wikipedia
from django.http import Http404

# Create your views here.
'''
def index(request):
    if request.method == 'GET':
        form = SearchForm(request.POST or None)
        if form.is_valid():

            title1 = form.cleaned_data['title1']
            title1.save()
            u = title1.replace(" ", "_")
            url = "https://en.wikipedia.org/wiki/"+u
            r= requests.get(url)
            soup = BeautifulSoup(r.content, "html.parser")
            data = soup.find("p").text
            
            return redirect("/")
    return render(request,'index.html')

'''


def index(request):
    
    return render(request, 'search/index.html', {})



'''
def result_view(request):
    if request.method == 'POST':
        search= request.POST.get('textfield') 
        print search
        u = search.replace(" ", "_")
        url = "https://en.wikipedia.org/wiki/"+u
        r= requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        data = soup.find("p").text
        s//oup.find('div',id="bodyContent").p
        return render(request,"result.html",{'search':search,'data':data})

    else:
        return render(request,"result.html",{})


'''
def result_view(request):
    if request.method == 'POST':
        search= request.POST.get('textfield') 
        
        print search
        try:
            try:
                value = wikipedia.page(search.encode('utf-8'))
                title= value.title
                url=value.url
                print title
                data= wikipedia.summary(search, sentences=10)

            except wikipedia.exceptions.DisambiguationError as e:
                data = e
                title=search+" (Disambiguation)"
                u = search.replace(" ", "_")
                url = "https://en.wikipedia.org/wiki/"+u

        except:
            raise Http404()
                
        return render(request,"search/result.html",{'title':title,'url':url,'data':data})

    else:
        return render(request,"search/result.html",{})

