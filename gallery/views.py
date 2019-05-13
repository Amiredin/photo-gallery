from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Category,Location,Image
from django.http import HttpResponse, Http404

# Create your views here.
def welcome(request):

    images = Image.get_images()
    context={'images': images}
    return render(request, 'index.html', context)
def singleimage(request, image_id):
    image = Image.objects.get(id=image_id)
    return render(request, 'singleimage.html', {'image': image})

def search_results(request):
    # categories = Category.objects.all()
    # print(categories)

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        images = Image.search_by_category(search_term)
        message = f"{search_term}"
        print(search_term)

        # context = {"images":images,"message":message}

        return render(request, 'search.html',{"images":images,"message":message})

    else:
        message = "You haven't searched for any term"
        # context={"message":message}
        return render(request, 'search.html',{"message":message})

def location_filter(request):

    images = Image.get_images()
    locations = Location.objects.all()
    return render(request,'location.html',{"images":images,"locations":locations})

# def location_images(request,location):
#     locations = Location.objects.all()
#     locationz = Location.get_location(location)
#     images = Image.filter_by_location(location)
#     title = f'{location} Photos'
#     return render(request, 'location.html', {'title':title, 'images':images, 'locations':locations, 'locationz':locationz})
