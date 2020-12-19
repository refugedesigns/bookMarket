from django.urls import path
from .views import (
    bookListView,
    bookDetailView,
    chapterDetailView,
    exerciseDetailView,
)

app_name = 'books'

urlpatterns = [
    path('', bookListView, name='book-list'),
    path('<slug>/', bookDetailView, name='book-detail'),
    path('<book_slug>/<chapter_number>/', chapterDetailView, name='chapter-detail'),
    path('<book_slug>/<chapter_number>/<exercise_number>/', exerciseDetailView, name='exercise-detail')
]
