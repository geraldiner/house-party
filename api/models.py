from django.db import models
import string
import random


def generate_unique_code():
    length = 6

    while True:
        code = "".join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break

    return code


# Create your models here.
class Room(models.Model):
    # code to join the room
    code = models.CharField(max_length=8, default="", unique=True)
    # host of the room
    host = models.CharField(max_length=50, unique=True)
    # boolean value for whether or not guests can pause or not
    guest_can_pause = models.BooleanField(null=False, default=False)
    # number of votes to skip a song
    votes_to_skip = models.IntegerField(null=False, default=1)
    # date/time the room is created
    created_at = models.DateTimeField(auto_now_add=True)
