
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import homeView, bookDetailView, cartView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='home'),
    path('book-detail/', bookDetailView, name='book-detail'),
    path('cart/', cartView, name='cart')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
