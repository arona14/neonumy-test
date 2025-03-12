from django.test import TestCase
from django.urls import reverse
from .models import Image

class ImageTests(TestCase):
    def setUp(self):
        self.image = Image.objects.create(title='Test Image', image='images/test.jpg')

    def test_image_listing(self):
        response = self.client.get(reverse('image_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Image')

    def test_image_detail(self):
        response = self.client.get(reverse('image_detail', args=[self.image.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Image')

    def test_image_upload(self):
        with open('media/images/test_image.jpeg', 'rb') as img:
            response = self.client.post(reverse('upload_image'), {'title': 'New Image', 'image': img})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Image.objects.count(), 2)

    def test_image_delete(self):
        response = self.client.post(reverse('delete_image', args=[self.image.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Image.objects.count(), 0)
