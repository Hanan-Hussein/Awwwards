from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    profilephoto = CloudinaryField("profilephoto")
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def _str_(self):
        return self.user.username

    @classmethod
    def save_profile(cls, profile):
        cls.save(profile)

    @classmethod
    def update_profile(cls, username, email, bio, profilephoto):
        cls.update(username=username, email=email,
                   bio=bio, profilephoto=profilephoto)

    @classmethod
    def delete_profile(cls, profile):
        cls.delete(profile)

class Project(models.Model):
    title = models.CharField(max_length=60,blank=False)
    landing_page = CloudinaryField("landing_page")
    site_url = models.URLField()
    description = models.TextField()
    owner = models.ForeignKey(User,related_name="projects",null=True,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title
