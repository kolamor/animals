from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

__all__ = ('UserProfile', 'Animal', 'AnimalType', 'ImageAnimal', )

User = get_user_model()


def generate_filename(instance, filename):
    filename = f'{instance.user}/animals/{instance.slug}/{filename.split(".")[0]}.{filename.split(".")[1]}'
    return filename


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    avatar = models.ImageField('аватар', upload_to='users/%Y/%m/%d/', blank=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return str(self.user)


class AnimalType(models.Model):
    type_animal = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Тип животного'
        verbose_name_plural = 'Типы животных'

    def __str__(self):
        return str(self.type_animal)


class Animal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField('slug', max_length=50)
    animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=generate_filename, blank=True)
    description = models.TextField()
    date_of_birth = models.DateField(blank=True, null=True)
    like = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'

    def __str__(self):
        return str(self.name)


class ImageAnimal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, verbose_name='петомец', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=generate_filename, blank=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'Фото Питомца'
        verbose_name_plural = 'Фото Питомцев'

    def __str__(self):
        return str(self.photo)


