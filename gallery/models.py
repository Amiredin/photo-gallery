from django.db import models
import datetime as dt


# Create your models here.
#
class Category(models.Model):
    name = models.CharField(max_length =20,default='Travel')

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def get_category_id(cls, id):
        category = Category.objects.get(pk = id)
        return category
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=20,default="Nairobi")
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    @classmethod
    def get_location(cls):
        locations = cls.objects.all()
        return locations
    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length = 60)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    location = models.ManyToManyField(Location)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to = 'gallery/')
    def __str__(self):
        return self.name

    def save_image(self):
        self.save()
    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id= id).all()
        return image

    def delete_image(self):
        self.delete()
    @classmethod
    def update_image(cls,id ,name, description ,location,category):
        updated_image = cls.objects.filter(id = id).update(name = name, description = description ,location = location,category = category)

    @classmethod
    def get_images(cls):
        images = Image.objects.all()
        return images
    @classmethod
    def search_by_category(cls,search_term):
        images_in_category = cls.objects.filter(category__name__icontains=search_term)
        return images_in_category
    @classmethod
    def filter_by_location(cls,id):
        images_location = Image.objects.filter(id=location.id)
        return images_location
        
    class Meta:
        ordering = ['name']