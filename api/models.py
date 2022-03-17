from django.db import models
import string
import random

# helper function to generate a unique code for each Room
def generate_unique_code():
    # set a pre-determined length of the code
    length = 6

    # while True - generate a code by calling random.choices on all the uppercase letters. it should return a list of letters of size = length. then join the letters in that list and save to code
    while True:
        code = "".join(random.choices(string.ascii_uppercase, k=length))
        # from the list of all existing Room objects, filter for those where their code is equal to the code generated here. if the list is empty (i.e., no other room with this code exists), break out of the loop and return the code
        if Room.objects.filter(code=code).count() == 0:
            break

    return code


# Room class for virtual rooms that plays music with controls
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
