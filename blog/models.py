import uuid
from django.db import models
from django.contrib.auth.hashers import make_password


def get_file_path(_instance, filename: str) -> str:
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    created = models.DateField('created', auto_now_add=True)
    modified = models.DateField('modified', auto_now=True)
    active = models.BooleanField('active', default=True)

    class Meta:
        abstract = True


class User(Base):
    name = models.CharField('name', max_length=100, null=False)
    description = models.TextField('description', max_length=500, null=False)
    email = models.CharField('email', max_length=100, null=False)
    password = models.CharField('password', max_length=100, null=False)
    image = models.ImageField(
        'image', upload_to=get_file_path, max_length=100)
    facebook = models.CharField(
        'Facebook', max_length=50, null=True, blank=True)
    twitter = models.CharField(
        'Twitter', max_length=50, null=True, blank=True)
    instagram = models.CharField(
        'Instagram', max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self) -> str:
        return self.name
