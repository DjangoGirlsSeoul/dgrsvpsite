# Seminars / Hacks
### For example : Hack@Seoul Seminar : Getting started w/ Arduino, Raspberry Pi, beacons and brain readers

## Proposed Model

  class Hack(models.Model):
    title  = models.CharField(max_length=200)
    short_description = models.CharField(max_length=400)
    long_description =  models.TextField()
    github_link = models.URLField(max_length=250, blank=True)
    ppt_link = models.URLField(max_length=250, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    cover_photo =  models.ImageField(upload_to='uploads',blank=True)
    category  = models.ManyToManyField(Category, blank=True, null=True, through='CategoryToHack')
    writer = models.ForeignKey(User)


    class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=60, unique=True)
    description = models.TextField()

    class CategoryToHack(models.Model):
      hack = models.ForeignKey(Hack)
      category = models.ForeignKey(Category)
