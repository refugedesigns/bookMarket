from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Book, Chapter, Exercise


# Create your views here.


def bookListView(request):
    queryset = Book.objects.all()
    context = {
        'books': queryset
    }
    return render(request, 'book_list.html', context)


def bookDetailView(request, slug):
    book = get_object_or_404(Book, slug=slug)
    context = {
        'book': book
    }
    return render(request, 'book_detail.html', context)


def chapterDetailView(request, book_slug, chapter_number):
    chapter_qs = Chapter.objects \
        .filter(books__slug=book_slug) \
        .filter(chapter_number=chapter_number)
    if chapter_qs.exists():
        context = {
            'chapter': chapter_qs[0]
        }
        return render(request, 'chapter_detail.html', context)
    return Http404

def exerciseDetailView(request, book_slug, chapter_number, exercise_number):
    exercise_qs = Exercise.objects \
        .filter(chapter__books__slug=book_slug) \
        .filter(chapter__chapter_number=chapter_number) \
        .filter(exercise_number=exercise_number)
    if exercise_qs.exists():
        context = {
            'exercise': exercise_qs[0]
        }
        return render(request, 'exercise_detail.html', context)
    return Http404


def cartView(request):
    context = {}
    return render(request, 'cart.html')
