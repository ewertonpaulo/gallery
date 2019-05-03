from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from .models import Photo
from django.contrib.auth.decorators import login_required
from .forms import photo_form


def index(request):
    photos = Photo.objects.filter(reviewed=True)
    paginator = Paginator(photos, 5)
    page = request.GET.get('page', 1)
    photos = paginator.get_page(page)
    return render(request, 'gallery.html', { 'photos':photos})

def add_photo(request):
    if request.method == 'POST':
        form = photo_form(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('index')
    else:
        form = photo_form()
    return render(request, 'add_photo.html', {'form':form})

@login_required
def list_photos(request):
    user = request.user
    photos = Photo.objects.filter(reviewed=False)
    return render(request, 'review.html', {'user': user, 'photos':photos})

@login_required
def delete_photo(request, id):
    photo = Photo.objects.get(id=id)
    photo.delete()
    return redirect('list_photos')

@login_required
def review(request, id):
    photo = Photo.objects.get(id=id)
    photo.reviewed = True
    photo.save()
    return redirect('list_photos')