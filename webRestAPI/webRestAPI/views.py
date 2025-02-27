from django.shortcuts import render
from urllib import request as req
import json

def home(request):
    return render(request,"home.html")

def studentsall(request):
    #  mysql cloud aws database 
    response = req.urlopen("http://127.0.0.1:5002/students/all")
    data = response.read()
    info = json.loads(data)
    data = {'info': info}
    return render(request, "allstudent.html", data)

def allbooks(request):
    #mongodb cloud atlas database 
    response = req.urlopen("http://127.0.0.1:5000/books/all")
    data = response.read()
    info = json.loads(data)
    data = {'info': info}
    return render(request, "allbooks.html", data)

def playernation(request):
  if request.method=="POST":
    na=request.POST.get("nation")
    response = req.urlopen("http://127.0.0.1:5001/player/"+na)
    data = response.read()
    info = json.loads(data)
    data = {'info': info}
    return render(request, "player.html", data)