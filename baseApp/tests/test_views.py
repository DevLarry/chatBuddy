from django.test import TestCase, Client
from baseApp.models import User, Message, Room, Topic
from django.urls import reverse, resolve
import json
from baseApp.views import home, logoutUser, registerUser


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.userProfile = reverse('profile', args=[1])
        self.user1 = User.objects.create(
            name = 'Ahmed',
            email = 'ahmed@gmail.com'
        )
        self.topics_url = reverse('topics')
        self.activity_url = reverse('activity')
        self.logout_url = reverse('logout')
        self.loginUser_url = reverse('login')
        self.registerUser_url = reverse('register')
        

    def test_home_view_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/home.html')
        self.assertTemplateUsed(response, 'base/components/roomAvail.html')
        self.assertTemplateUsed(response, 'base/components/browse.html')
        self.assertTemplateUsed(response, 'base/components/activity.html')
    
    def test_userProfile_view_POST(self):
        response = self.client.post(self.userProfile)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/profile.html')
    
    def test_topics_view_GET(self):
        response = self.client.get(self.topics_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/topics.html')
    
    def test_activity_view_GET(self):
        response = self.client.get(self.activity_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/activity.html')
    
    def test_logout_view_GET(self):
        response = self.client.get(self.logout_url)
        #Redirect status code is 302
        self.assertEquals(response.status_code, 302)
        self.assertEquals(resolve(self.logout_url).func, logoutUser)
    
    def test_login_view_GET(self):
        response = self.client.get(self.loginUser_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/login.html')
    
    def test_register_view_GET(self):
        response = self.client.get(self.registerUser_url)
        #Redirect status code is 302
        self.assertEquals(response.status_code, 200)
        print(resolve(self.registerUser_url))
        self.assertEquals(resolve(self.registerUser_url).func, registerUser)