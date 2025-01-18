from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Topic, Entry

class LearningLogViewsTestCase(TestCase):

    def setUp(self):
        """Przygotowanie danych testowych."""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

        # Tworzenie przykładowego tematu i wpisu
        self.topic = Topic.objects.create(text='Test Topic', owner=self.user)
        self.entry = Entry.objects.create(topic=self.topic, text='Test Entry')

    def test_index_view(self):
        """Test widoku strony głównej."""
        response = self.client.get(reverse('learning_logs:index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('learning_logs/index.html', [t.name for t in response.templates])

    def test_topics_view(self):
        """Test widoku topics."""
        response = self.client.get(reverse('learning_logs:topics'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('learning_logs/topics.html', [t.name for t in response.templates])
        self.assertContains(response, 'Test Topic')

    def test_topic_view(self):
        """Test widoku topic."""
        response = self.client.get(reverse('learning_logs:topic', args=[self.topic.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIn('learning_logs/topic.html', [t.name for t in response.templates])
        self.assertContains(response, 'Test Topic')
        self.assertContains(response, 'Test Entry')

    def test_new_topic_view(self):
        """Test dodawania nowego tematu."""
        response = self.client.post(reverse('learning_logs:new_topic'), {'text': 'New Test Topic'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Topic.objects.filter(text='New Test Topic', owner=self.user).exists())

    def test_new_entry_view(self):
        """Test dodawania nowego wpisu."""
        response = self.client.post(reverse('learning_logs:new_entry', args=[self.topic.id]), {'text': 'New Test Entry'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Entry.objects.filter(text='New Test Entry', topic=self.topic).exists())

    def test_edit_entry_view(self):
        """Test edycji istniejącego wpisu."""
        response = self.client.post(reverse('learning_logs:edit_entry', args=[self.entry.id]), {'text': 'Edited Test Entry'})
        self.assertEqual(response.status_code, 302)
        self.entry.refresh_from_db()
        self.assertEqual(self.entry.text, 'Edited Test Entry')

    def test_topic_access_restriction(self):
        """Test ograniczenia dostępu do tematu należącego do innego użytkownika."""
        other_user = User.objects.create_user(username='otheruser', password='password456')
        other_topic = Topic.objects.create(text='Other User Topic', owner=other_user)
        response = self.client.get(reverse('learning_logs:topic', args=[other_topic.id]))
        self.assertEqual(response.status_code, 404)

    def test_edit_entry_access_restriction(self):
        """Test ograniczenia edycji wpisu należącego do innego użytkownika."""
        other_user = User.objects.create_user(username='otheruser', password='password456')
        other_topic = Topic.objects.create(text='Other User Topic', owner=other_user)
        other_entry = Entry.objects.create(topic=other_topic, text='Other User Entry')
        response = self.client.post(reverse('learning_logs:edit_entry', args=[other_entry.id]), {'text': 'Hacked Entry'})
        self.assertEqual(response.status_code, 404)
