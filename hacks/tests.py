from django.test import TestCase
from hacks.models import Hack,Category
from django.contrib.auth.models import User

class HackTestCase(TestCase):
    def setUp(self):
        cat = Category.objects.create(title="testcat",slug="test",description="test")
        u = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        hack1 = Hack.objects.create(title="lion", short_description="roar",long_description="bam", github_link="google", ppt_link="google.com",writer=u)
        hack1.category.add(cat)
        hack2 = Hack.objects.create(title="cat", short_description="roar",long_description="bam", github_link="google", ppt_link="google.com",writer=u)
        hack2.category.add(cat)

    def test_hack_have_title(self):
        """Hack Test"""
        hack1 = Hack.objects.get(title="lion")
        cat1 = hack1.category.all()[0]
        hack2 = Hack.objects.get(title="cat")
        self.assertEqual(hack1.title, 'lion')
        self.assertEqual(cat1.title, "testcat")
        self.assertEqual(hack2.short_description, 'roar')
