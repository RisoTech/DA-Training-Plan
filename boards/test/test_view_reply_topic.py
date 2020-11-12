
from django.contrib.auth.models import User
from ..models import Board, Topic, Post
from django.test import TestCase
from django.urls import reverse, resolve

class ReplyTopicTestCase(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='django', description='hello website')
        self.username = 'donga123'
        self.password = '1234abcd'
        user = User.objects.create_user(username=self.username,email='donga.ftu2@gmail.com', password=self.password)
        self.topic = Topic.objects.create(board=self.board, starter=user, subject='hello world')
        Post.objects.create(message='no one see me', topic=self.topic, created_by=user)
        self.url = reverse('reply_topics', kwargs={'pk':self.board.pk, 'topic_pk':self.topic.pk})
    
# class LoginRequiredReplyTopicTests(ReplyTopicTestCase):

# class ReplyTopicTest(ReplyTopicTestCase):

class SuccessfullReplyTopicTest(ReplyTopicTestCase):
    def test_redirection(self):
        '''
        A valid form submission should redirect the user
        '''
        url = reverse('topic_posts', kwargs={'pk': self.board.pk, 'topic_pk': self.topic.pk})
        topic_posts_url = '{url}?page=1#2'.format(url=url)
        self.assertRedirects(self.response, topic_posts_url)

# class InvalidReplyTopicTest(ReplyTopicTestCase):




