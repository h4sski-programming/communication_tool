from django.test import TestCase
from django.urls import reverse

# from .views import index, aaa, bbb

# Create your tests here.

class ViewsTests(TestCase):
    
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'index.html')
        
    def test_create_team_view(self):
        response = self.client.get(reverse('create_team'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_team.html')