from django.shortcuts import redirect, render, HttpResponse

from . models import *

# Create your views here.
def index(request):
    print(Book.objects.all())
    context = {

        "allBooks": Book.objects.all()
    }
    return render(request, "mark.html", context)

def addingBooks(request):
    print("*****************")
    print(request.POST)
    print("*****************")
    # Book.objects.create(title = "Python")
    Book.objects.create(title = request.POST["booktitle"], desc = request.POST["desc"])
    return redirect("/")

def showbookinfo(request , idBook):
    print("*****************")
    print(Book.objects.get(id=idBook))
    print("*****************")
    context = {

        "oneBooks": Book.objects.get(id=idBook),
        "allAuthor": Author.objects.all()
    }
    return render(request, "bookinfo.html", context)

def anotherone(request, idBook):
    print(request.POST)
    this_Author = Author.objects.get(id=request.POST["selectAuthor"])
    Author.objects.get(id=request.POST["selectAuthor"]).notes.add(Book.objects.get(id=idBook))
    print("*****************", this_Author)
    return redirect("/")