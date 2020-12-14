from django.shortcuts import render

# Create your views here.


def homeView(request):
    context = {}
    return render(request, 'book_list.html', context)

def bookDetailView(request):
    context = {}
    return render(request, 'book_detail.html', context)

def cartView(request):
    context = {}
    return render(request, 'cart.html')