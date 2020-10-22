from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your models here

class Profile(models.Model):
    FICTION = 'FC'
    ENGINEERING = 'ER'
    SCIENCE = 'SC'
    MANAGEMENT = 'MG'
    LITERATURE = 'LT'
    ARTS = 'AR'
    SCHOOL = 'SC'
    RELIGION = 'RG'
    ENTRANCE = 'ET'
    GOVERNMENT = 'GR'
    MISC = 'MI'
    LAW = 'LA'
    CATEGORY_CHOICES = [
        (FICTION, 'fiction'),
        (ENGINEERING, 'Engineering'),
        (SCIENCE, 'Science'),
        (MANAGEMENT, 'Managemetn'),
        (LITERATURE, 'Literature'),
        (ARTS, 'Arts'),
        (SCHOOL, 'School Level'),
        (RELIGION, 'Religion'),
        (LAW, 'Law'),
        (ENTRANCE, 'Entrance Preparation'),
        (GOVERNMENT,'Government Jobs'),
        (MISC, 'Miscelleneous'),
    ]

    INDIVIDUAL_SELLER = 'IS'
    WHOLESELLER = 'WS'
    OTHER = 'OT'
    CATEGORY_SELLER = [
        (INDIVIDUAL_SELLER, 'Individual Seller'),
        (WHOLESELLER, 'Wholeseller'),
        (OTHER, 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=15)
    profession = models.CharField(max_length=100)
    interest = models.CharField(choices=CATEGORY_CHOICES,default=MISC,max_length=100)
    profile_image = models.ImageField(upload_to='media')
    user_type = models.CharField(choices=CATEGORY_SELLER,default=INDIVIDUAL_SELLER,max_length=100)
    rating = models.CharField(max_length=50)
    pradesh = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    palika = models.CharField(max_length=50)
    ward_no = models.IntegerField()
    local_add = models.CharField(max_length=50)





class Product(models.Model):
    FICTION = 'FC'
    ENGINEERING = 'ER'
    SCIENCE = 'SC'
    MANAGEMENT = 'MG'
    LITERATURE = 'LT'
    ARTS = 'AR'
    SCHOOL = 'SC'
    RELIGION = 'RG'
    ENTRANCE = 'ET'
    GOVERNMENT = 'GR'
    MISC = 'MI'
    LAW = 'LA'
    CATEGORY_CHOICES = [
        (FICTION, 'fiction'),
        (ENGINEERING, 'Engineering'),
        (SCIENCE, 'Science'),
        (MANAGEMENT, 'Managemetn'),
        (LITERATURE, 'Literature'),
        (ARTS, 'Arts'),
        (SCHOOL, 'School Level'),
        (RELIGION, 'Religion'),
        (LAW, 'Law'),
        (ENTRANCE, 'Entrance Preparation'),
        (GOVERNMENT,'Government Jobs'),
        (MISC, 'Miscelleneous'),
    ]
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media')
    details = models.TextField()
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.CharField(max_length=6)
    published_date = models.DateTimeField(auto_now_add=True, blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES,default=MISC,max_length=100)
    featured = models.BooleanField()

class admin(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.EmailField(null=False,blank=False)

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    desc = models.TextField()