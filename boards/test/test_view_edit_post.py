from django.core.checks import messages
from django.test import TestCase
from ..models import Board, Topic, Post
from ..views import PostUpdateView
from django.urls import reverse, resolve
from django.contrib.auth.models import User

class PostUpdateViewTestCase(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='So django is good')
        self.username ='donga123'
        self.password = '1234abcd'
        user = User.objects.create_user(username=self.username, email='donga.ftu2@gmail.com', password=self.password)
        self.topic = Topic.objects.create(subject='test case', starter=user, board=self.board)
        self.post = Post.objects.create(message='Hello there', created_by=user, topic=self.topic)
        self.url = reverse('edit_post', kwargs={'pk': self.board.pk, 'topic_pk':self.topic.pk, 'post_pk':self.post.pk})

class LoginRequiredPostUpdateViewTests(PostUpdateViewTestCase):
    def Test_redirection(self):
        # When go into this url, redirect to 'login page'
        response = self.client.get(self.url)
        login_url = reverse('login')
        self.assertRedirects(response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))

class UnauthorizedPostUpdateViewTest(PostUpdateViewTestCase):
    def setUp(self):
        super().setUp()
        username='hientran123'
        password='12345abcde'
        user = User.objects.create_user(username=username, email='fengftu@gmail.com', password=password)
        self.client.login(username=username, password=password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 404)


