from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class User(AbstractUser):
    email = models.EmailField(blank=False, max_length=50, verbose_name="email address")
    gender = models.CharField(max_length=20)
    saved_trips = models.TextField() ## To do 
    about = models.TextField(blank=True)
    trip_status = models.BooleanField(default=False)
    joined_at = datetime.datetime.now()

    USERNAME_FIELD = "username"   # e.g: "username", "email"
    EMAIL_FIELD = "email"         # e.g: "email", "primary_email"

class UserFollowing(models.Model):
    user_id = models.ForeignKey(User, related_name="following", on_delete=models.DO_NOTHING)
    following_user_id = models.ForeignKey(User, related_name="followers", on_delete=models.DO_NOTHING)

    # Even add info about when user started following
    created = models.DateTimeField(auto_now_add=True)
    


    ## Now, in your post method implementation, you would do only this:
    # UserFollowing.objects.create(user_id=user.id,
    #                             following_user_id=follow.id)

    ## And then, you can access following and followers easily:
    # user = User.objects.get(id=1) # it is just example with id 1
    # user.following.all()
    # user.followers.all()