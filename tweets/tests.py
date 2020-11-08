from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Tweet
# Create your tests here.
User = get_user_model()

class TweetTestCase(TestCase):
    def setUp(self): #used to create instacnce
        self.user = User.objects.create_user(username='adi',password='somepassword')


    def test_tweet_(self):
        self.assertEqual(self.user.username,"adi")
        self.assertEqual(1, 2)