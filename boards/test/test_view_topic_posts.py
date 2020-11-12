from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.urls import reverse, resolve

from ..models import *
from ..views import PostListView

class TopicPostsTests(TestCase):
    def setUp(self):
        board = Board.objects.create(name='django', description='Hello world, Today I will teach you abut django')
        user = User.objects.create_user(username='john', email='john_dev@gmail.com', password='1234abcdE')
        topic = Topic.objects.create(subject='Hello',board=board, starter=user)
        Post.objects.create(message='Fuck ya!', topic=topic, created_by=user)
        url = reverse('topic_posts', kwargs={'pk':board.pk, 'topic_pk':topic.pk})
        self.response = self.client.get(url)
    
    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)
    
    def test_view_function(self):
        view = resolve('/boards/1/topics/1/')
        self.assertEquals(view.func.view_class, PostListView)

