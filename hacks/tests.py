from django.test import TestCase
from hacks.models import Hack,Category
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class HackTestCase(TestCase):
    def setUp(self):
        cat1 = Category.objects.create(title="test cat",description="test")
        cat2 = Category.objects.create(title="test lion",description="test")
        u = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        hack1 = Hack.objects.create(title="title lion", short_description="roar",long_description="bam", github_link="google", ppt_link="google.com",writer=u)
        hack1.category.add(cat1)
        hack2 = Hack.objects.create(title="title cat", short_description="roar",long_description="bam", github_link="google", ppt_link="google.com",writer=u)
        hack2.category.add(cat2)

    def test_hack_have_title(self):
        """Hack Test
            Fields tested : title,slug,short_description,category
        """
        hack1 = Hack.objects.get(title="title lion")
        cat1 = hack1.category.all()[0]
        hack2 = Hack.objects.get(title="title cat")
        cat2 = hack2.category.all()[0]
        self.assertEqual(hack1.title, 'title lion')
        self.assertEqual(cat1.title, "test cat")
        self.assertEqual(hack2.short_description, 'roar')
        self.assertEqual(hack1.slug, 'title-lion')
        self.assertEqual(hack2.slug, 'title-cat')
        self.assertEqual(cat2.slug, 'test-lion')

class HackViewTests(TestCase):
    def test_hack_index_page(self):
        response = self.client.get(reverse('hacks:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'No posts available')
