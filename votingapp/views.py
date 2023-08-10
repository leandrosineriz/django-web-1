from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
arr = ["Javascript","Python",'Go','Java','Kotlin','PHP','C#','Swift','R','Ruby','C','C++','Matlab','TypeScript','Scala','SQL','HTML','CSS','NoSQL','Rust','Perl']
globalcnt = dict()
max = 0

def index(request):
    set_max()
            
    mydictionary = {
        "arr" : arr,
        "globalcnt" : globalcnt,
        "max" : max
    }
    
    
            
    return render (request, 'votingapp/index.html', context=mydictionary)

def getquery(request):
    q = request.GET["languages"]
    if q in arr:
        if q in globalcnt:
            #if already exist the increment the value
            globalcnt[q]+=1
        else:
            #first occurrence
            globalcnt[q]=1
            
    set_max()
            
    mydictionary = {
        "arr": arr,
        "globalcnt": globalcnt,
        "max" : max
    }
    return render(request, "votingapp/index.html", context=mydictionary)

def sortdata(request):
    global globalcnt
    global max
    
    globalcnt = dict(sorted(globalcnt.items(), key=lambda x:x[1], reverse=True))
    
    set_max()
    
    mydictionary = {
        "arr" : arr,
        "globalcnt" : globalcnt,
        "max" : max
    }
    return render (request, 'votingapp/index.html', context=mydictionary)

def set_max():
    global max
    global globalcnt
    
    for key, value in globalcnt.items():
        if value > max:
            max = value