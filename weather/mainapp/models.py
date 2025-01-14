from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('recipe-detail', kwargs={'pk': self.pk})

class Weather(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=50)


    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('recipe-detail', kwargs={'pk': self.pk})
