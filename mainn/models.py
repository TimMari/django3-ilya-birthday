from django.db import models


class MainImg(models.Model):
   photo = models.ImageField('Фото для шапки сайта', upload_to='mainn/mainImg/')


class Info(models.Model):
   title = models.CharField('Заголовок', max_length=50)
   text = models.TextField('Текст о себе')
   photo = models.ImageField('Фото', upload_to='mainn/infoImg/', blank=True)


   def __str__(self):
      return self.title


class VidSport(models.Model):
   title = models.CharField('Название', max_length=50)
   url = models.URLField('Ссылка')
   video = models.FileField('Видео', upload_to='mainn/spv/', blank=True)


   def __str__(self):
      return self.title



class VidGame(models.Model):
   title = models.CharField('Название', max_length=50)
   url = models.URLField('Ссылка')
   video = models.FileField('Видео', upload_to='mainn/spv/', blank=True)


   def __str__(self):
      return self.title


class VidOther(models.Model):
   title = models.CharField('Название', max_length=50)
   url = models.URLField('Ссылка')
   video = models.FileField('Видео', upload_to='mainn/spv/', blank=True)


   def __str__(self):
      return self.title



class BlogModel(models.Model):
   title = models.CharField('Название', max_length=50)
   description = models.TextField('Описание')
   img = models.ImageField('Фото', upload_to='mainn/blogImg/', blank=True)
   audio = models.FileField('Музыка', upload_to='mainn/blogmus', blank=True)
   url = models.URLField('Ссылка', blank=True)

   def __str__(self):
      return self.title

