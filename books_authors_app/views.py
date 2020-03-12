from django.shortcuts import render, redirect
from .models import *
def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, "index.html", context)
def add_author(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, "add_author.html", context)
def render_book(request, book_num):
    context = {
        'books': Book.objects.get(id=book_num),
        'authors': Author.objects.all()
    }
    return render(request, "render_book.html", context)
def render_author(request, author_num):
    context = {
        'authors': Author.objects.get(id=author_num),
        'books': Book.objects.all()
    }
    return render(request, "render_author.html", context)
def book(request):
    title = request.POST["title"]
    description = request.POST["description"]
    Book.objects.create(title = title, description = description)
    return redirect("/")
def author(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    notes = request.POST["notes"]
    Author.objects.create(first_name = first_name, last_name = last_name, notes = notes)
    return redirect("/add_author")
def book_author(request, book_num):
    this_book = Book.objects.get(id=book_num)
    this_author = Author.objects.get(id=request.POST['Author'])
    this_author.books.add(this_book)
    return redirect(f"/render_book/{book_num}")
def author_book(request, author_num):
    this_book = Book.objects.get(id=request.POST['Book'])
    this_author = Author.objects.get(id=author_num)
    this_book.authors.add(this_author)
    return redirect(f'/render_author/{author_num}')
def home(request):
    return redirect("/")