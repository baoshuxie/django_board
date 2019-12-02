from django.test import TestCase
from django.urls import resolve,reverse
from django.contrib.auth.models import User
from ..models import Board, Post, Topic
from ..views import PostListView

class TopicPostsTests(TestCase):
	def setUp(self):
		board = Board.objects.create(name='Django',description='Django Board')
		user = User.objects.create_user(username='john',email='john@doe.com',password='123')
		topic = Topic.objects.create(subject = 'hello world',board=board,starter=user)
		Post.objects.create(message = 'lorem ipsum',topic=topic)
		url = reverse('topic_posts',kwargs={'pk':board.pk,'topic_pk':topic.pk})
		self.response = self.client.get(url)

	def test_status_code(self):
		self.assertEquals(self.response.status_code,200)

	def test_view_function(self):
		view = resolve('/boards/1/topics/1/')
		self.assertEquals(view.func.view_class,PostListView)