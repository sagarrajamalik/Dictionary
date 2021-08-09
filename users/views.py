from django.contrib import auth
from django.shortcuts import render, redirect

import requests
from numpy import random



def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")






def movieforyou(request):
    try:

        word=request.GET['word']
        a=requests.get("https://api.dictionaryapi.dev/api/v2/entries/en_US/"+word)
        meaning=a.json()

        ans=meaning[0]['meanings'][0]['definitions'][0]['definition']
    except:

        ans = "Word is invalid as per US English"





    return render(request,"movieforyou.html",{'ans':ans})