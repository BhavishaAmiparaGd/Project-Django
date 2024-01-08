from django.shortcuts import render

from django.http import HttpResponse

def home(request):
     # return HttpResponse("hey i am django server");

     people = [
         {'name':"bhavisha",'age':20},
         {'name':'hetakxi','age':11},

     ]

     for i in people:
         if i['age']:
             print("yes")

     text = '''Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph.'''
     vegetables = ['pumpkin','Tomato','Potato']

     return render(request, "home/index.html",context={'page':'Django practice', "people":people,"text":text,'vegetables':vegetables})


def about(request):
    context = {'page': 'About'}
    return render(request, "home/about.html",context)


def contact(request):
    context = {'page':'Contact'}
    return render(request, "home/contact.html",context)


def success_page(request):
    return HttpResponse("this is my success page")