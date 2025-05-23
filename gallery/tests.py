# tests.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_gallery.settings')
django.setup()


from django.test import TestCase
from .models import Category, Image
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime


class CategoryModelTest(TestCase):

    def test_category_str(self):
        category = Category.objects.create(name='Nature')
        self.assertEqual(str(category), 'Nature')


class ImageModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Art')
        self.image_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'small test image',
            content_type='image/jpeg'
        )

    def test_image_creation(self):
        image = Image.objects.create(
            title='Test Image',
            image=self.image_file,
            age_limit=18
        )
        image.categories.add(self.category)

        self.assertEqual(str(image), 'Test Image')
        self.assertEqual(image.age_limit, 18)
        self.assertEqual(image.categories.count(), 1)
        self.assertEqual(image.categories.first().name, 'Art')
        self.assertEqual(image.created_date, datetime.date.today())
