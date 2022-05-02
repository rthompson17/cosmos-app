from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    event_type = models.CharField(max_length=100)
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    has_party = models.BooleanField()
    description = models.CharField(max_length=600)
    users_watching = models.ManyToManyField(User, related_name='users_watching_event')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_created_by_user')

    def __str__(self):
        return f"Event is {self.title} in {self.location}."
    
class Profile(models.Model):
    photo_url = models.CharField(max_length=255)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    google_id = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"This is the profile of {self.user}"

class Photo(models.Model):
    url = models.CharField(max_length=255)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo at {self.url}"

class ViewingParty(models.Model):
    name = models.CharField(max_length=100)
    party_location = models.CharField(max_length=100)
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='party_created_by_user')
    description = models.CharField(max_length=500)
    attendees = models.ManyToManyField(User, related_name='party_attendees')

    def __str__(self):
        return f"Viewing party is {self.name}."