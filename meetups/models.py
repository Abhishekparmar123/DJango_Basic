from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.address}, {self.name}'


class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    org_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    describe = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participant = models.ManyToManyField(Participant, blank=True, null=True)

    def __str__(self):
        return f'{self.title}-{self.slug}'
