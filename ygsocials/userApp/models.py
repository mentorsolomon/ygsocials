from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class UserProfile(models.Model):
    gender = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('I had rather not say', 'I had rather not say'),
        ('LGBTQ', 'LGBTQ'),
        ('Others', ('Others'))
    ]

    Countries = [
        ('Angola', 'Angola'),
        ('Canada', 'Canada'),
        ('Kamataj', 'Kamataj'),
        ('Nigeria', 'Nigeria'),
        ('United Kingdom', 'United Kingdom'),
        ('United States of America', 'United States of America'),
        ('Others', 'Others'),
    ]

    Social_media = [
    ('X', 'X'),
    ('Facebook', 'Facebook'),
    ('Instagram', 'Instagram'),
    ('LinkedIn', 'LinkedIn'),
    ('Others','Others'),
    ]

    Followers = [
        ('0001-4999', '0001-4999'),
        ('5000-9999', '5000-9999'),
        ('10_000-50_000', '10_000-50_000'),
        ('50k Above', '50k Above'),
    ]

    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=16)
    address = models.CharField(max_length=255)
    social_media = models.CharField(choices=Social_media, max_length=90) 
    gender = models.CharField(choices=gender, max_length=250)
    country = models.CharField(choices=Countries, max_length=60)
    followers = models.CharField(choices=Followers, max_length=50)
    profile_view = models.ImageField(upload_to='Profile_view_images/', unique=False, null=True)
    client = models.BooleanField(default=False)
    HOD = models.BooleanField(default=False)



    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_user_receiver(sender, instance, **kwargs):
        instance.userprofile.save()
    