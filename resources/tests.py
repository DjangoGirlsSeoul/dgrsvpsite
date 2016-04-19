from django.test import TestCase
from resources.models import Resource,Category
from django.core.urlresolvers import reverse

class TestCase(TestCase):
    def setUp(self):
        cat1 = Category.objects.create(title="python")
        cat2 = Category.objects.create(title="django")
        resource1 = Resource.objects.create(title="title lion", link="http://python.org", category= cat1)
        resource2 = Resource.objects.create(title="title cat", link="http://djangoproject.com",category= cat2)

    def test_hack_have_title(self):
        """Resource Test
            Fields tested : title,slug,category
        """
        resource1 = Resource.objects.get(title="title lion")
        cat1 = resource1.category
        resource2 = Resource.objects.get(title="title cat")
        cat2 = resource2.category
        self.assertEqual(resource1.title, 'title lion')
        self.assertEqual(cat1.title, "python")
        self.assertEqual(resource2.slug, 'title-cat')
        self.assertEqual(cat2.slug, 'django')

class ResourceViewTests(TestCase):
    def test_resources_index_page(self):
        response = self.client.get(reverse('resources:index'))
        self.assertEqual(response.status_code, 200)
