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
    title = models.CharField(max_length=60, blank=False)
    landing_page = CloudinaryField("landing_page")
    site_url = models.URLField()
    description = models.TextField()
    owner = models.ForeignKey(
        User, related_name="projects", null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    @classmethod
    def save_project(cls, project):
        cls.save()

    @classmethod
    def delete_prject(cls, project_id):
        cls.delete(id=project_id)

    @classmethod
    def update_project(cls, title):
        cls.update(title=title)

    @classmethod
    def search_project(cls, title):
        project = cls.objects.filter(title__icontains=title)
        return project


class Ratings(models.Model):
    design = models.ForeignKey(
        Project, related_name="design", null=True, on_delete=models.CASCADE)
    usability = models.ForeignKey(
        Project, related_name="usability", null=True, on_delete=models.CASCADE)
    content = models.ForeignKey(
        Project, related_name="content", null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="users",
                             null=True, on_delete=models.CASCADE)
