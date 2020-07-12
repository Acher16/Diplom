from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Max

def get_new_default():
    if Ref.objects.all().count() == 0:
        new_number_default = 1
    else:
        new_number_default = Ref.objects.all().aggregate(Max('number'))['number__max'] + 1
    return new_number_default

class Ref(models.Model):
    slug = models.SlugField('Сокращенная ссылка')
    title = models.CharField('Пометка', max_length=50)
    site_url = models.CharField('Длинная ссылка', max_length=250)
    avtor = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField(default=get_new_default)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ref')
