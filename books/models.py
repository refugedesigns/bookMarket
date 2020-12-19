from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    slug = models.SlugField(blank=True)
    isbn = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='book_cover')
    price = models.FloatField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:book-detail', kwargs={'slug': self.slug})

class Chapter(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter_number = models.IntegerField()
    title = models.CharField(max_length=100)

    class Meta:
        ordering = ['chapter_number']

    def __str__(self):
        return f"{self.books.title} - {self.title}"

    def get_absolute_url(self):
        return reverse('books:chapter-detail', kwargs={
            'book_slug': self.books.slug,
            'chapter_number': self.chapter_number,
        })

class Exercise(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    exercise_number = models.IntegerField()
    page_number = models.IntegerField()
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('books:exercise-detail', kwargs={
            'book_slug': self.chapter.books.slug,
            'chapter_number': self.chapter.chapter_number,
            'exercise_number': self.exercise_number,
        })
    

class Solution(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    solution_number = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return f"{self.exercise.title}-{self.pk}"




