from django.shortcuts import render
from django.http import HttpResponse

class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
  Finch('Lolo', 'tabby', 'foul little demon', 3),
  Finch('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Finch('Raven', 'black tripod', '3 legged cat', 4)
]

# Create your views here.

def home(request):
  return HttpResponse('<h1>Hello Finchy</h1>')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })