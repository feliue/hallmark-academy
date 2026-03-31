from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Photo


def gallery(request):
    photos = Photo.objects.all().order_by('-date_uploaded')
    return render(request, 'gallery/gallery.html', {'photos': photos})
