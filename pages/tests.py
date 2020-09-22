from django.test import SimpleTestCase

# Create your tests here.

class SimpleTest(SimpleTestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    
    def test_info_page(self):
        response = self.client.get('/info/')
        self.assertEqual(response.status_code, 200)