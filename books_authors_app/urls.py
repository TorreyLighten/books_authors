from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add_author', views.add_author),
    path('book', views.book),
    path('author', views.author),
    path('render_author/<int:author_num>', views.render_author),
    path('render_book/<int:book_num>', views.render_book),
    path('book/author/<int:book_num>', views.book_author),
    path('author/book/<int:author_num>', views.author_book),
    path('home', views.home),
]