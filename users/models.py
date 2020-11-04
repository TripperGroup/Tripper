from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class User(AbstractUser):
    email = models.EmailField( max_length=100, verbose_name="email address", unique=True)
    gender = models.CharField(max_length=20, blank=True)
    about = models.TextField(blank=True)
    trip_status = models.BooleanField(default=False)
    joined_at = datetime.datetime.now()
    phone = models.CharField(null=True,max_length=50)
    avatar = models.ImageField(blank=True,null= True , upload_to='images/profile/avatar')
    header = models.ImageField(blank= True, null= True, upload_to='images/profile/header')

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = "username"   # e.g: "username", "email"
    EMAIL_FIELD = "email"         # e.g: "email", "primary_email"

class UserFollowing(models.Model):
    user_id = models.ForeignKey(User, related_name="following", on_delete=models.DO_NOTHING)
    following_user_id = models.ForeignKey(User, related_name="followers", on_delete=models.DO_NOTHING)

    # Even add info about when user started following
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_id', 'following_user_id',)
    


    ## Now, in your post method implementation, you would do only this:
    # UserFollowing.objects.create(user_id=user.id,
    #                             following_user_id=follow.id)

    ## And then, you can access following and followers easily:
    # user = User.objects.get(id=1) # it is just example with id 1
    # user.following.all()
    # user.followers.all()