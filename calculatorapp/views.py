from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "calculatorapp/index.html")

def submitquery(request):
    q = request.GET["query"]
    try:
        ans = eval(q)
        mydictionary = {
            "q" : q,
            "ans" : ans,
            "error" : False
        }
        return render(request, "calculatorapp/index.html", context=mydictionary)
    except:
        ans = 0
        mydictionary = {
            "q" : q,
            "ans" : ans,
            "error" : True
        }
        return render(request, "calculatorapp/index.html", context=mydictionary)
    