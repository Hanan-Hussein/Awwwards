from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Project,Ratings

# Create your tests here.

class UserTestClass(TestCase):
    def setUp(self):
        self.new_user=User(
            username='jaffar',email='jaff@gmail.com',password='pass1'
        )
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))

    def test_save_method(self):
        self.new_user.save()
        user=User.objects.all()
        self.assertEquals(len(user),1)
    
    def test_delete_method(self):
        self.new_user.save()
        self.new_user.delete()
        user = User.objects.all()
        self.assertFalse(User.objects.filter(pk=self.new_user.id).exists())

class ImagePostTestClass(TestCase):
    def setUp(self):
        self.user=User(
            username='jaffar',email='jaff@gmail.com',password='pass1'
    )
        self.user.save()

        self.image=Project(title='water',owner=self.user,landing_page='https://picsum.photos/200/300',description='Hey this is great',site_url='https://hjblog.azurewebsites.net/')

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Project))

    def test_save_profile(self):
        self.image.save()
        images = Project.objects.all()

        self.assertEquals(len(images),1)

    def test_delete_image(self):
        def setUp(self):
            self.user=User(
                username='jaffar',email='jaff@gmail.com',password='pass1')
        self.user.save()
        self.image=Project(id=1,title='water',owner=self.user,landing_page='https://picsum.photos/200/300',description='Hey this is great',site_url='https://hjblog.azurewebsites.net/')
        self.image.delete()
        images = Project.objects.all()

        self.assertFalse(Project.objects.filter(pk=self.image.id).exists())



class ProfileTestClass(TestCase):
  
    def setUp(self):
        self.user=User(
            username='bb',email='bb@gmail.com',password='pass1'
    )
        self.image=Project(title='water',owner=self.user,landing_page='https://picsum.photos/200/300',description='Hey this is great',site_url='https://hjblog.azurewebsites.net/')


        self.user.save()
        self.image.save()

 
    def test_save_profile(self):
        profiles = Profile.objects.all()

        self.assertEquals(len(profiles),1)

class RatingsTestCase(TestCase):

    def setUp(self):
        self.user=User(
            username='bb',email='bb@gmail.com',password='pass1'
    )
        self.image=Project(title='water',owner=self.user,landing_page='https://picsum.photos/200/300',description='Hey this is great',site_url='https://hjblog.azurewebsites.net/')

        self.user.save()
        self.image.save()
    def test_instance(self):
        self.project = Ratings(project = self.image,design = 5,usability=3,content=8,user=self.user)
        self.assertTrue(isinstance(self.project,Ratings))


