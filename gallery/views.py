from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Category,Location,Image
from django.http import HttpResponse, Http404

# Create your views here.
def welcome(request):
    location= Location.get_location()
    images = Image.get_images()
    return render(request, 'index.html',{'location':location,'images': images})
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

def location_filter(request,locate_id):

    images = Image.objects.filter(location=locate_id)
    location= Location.get_location()
    return render(request,'location.html',{"images":images,"locations":location})


