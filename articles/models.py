from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from sorl.thumbnail import ImageField, get_thumbnail
import datetime

class Articles(models.Model):

	class Meta():
		verbose_name = 'Article'
		verbose_name_plural = 'Articles'

	imageTitle = models.ImageField(upload_to='media/', blank=True, null=True)
	title = models.TextField()
	subtitle = models.TextField()
	content = RichTextUploadingField()
	datePublished = models.CharField(max_length=11, blank=True, null=True)
	viewCount = models.IntegerField(default=0)
	author = models.CharField(max_length=150, blank=True, null=True)
	slug = models.SlugField(blank=True, null=True)


	def save(self, *args, **kwargs):
		self.slug = self.title.replace(' ', '-')
		self.datePublished = datetime.datetime.now()
		super(Articles, self).save(*args, **kwargs)


	def __str__(self):
		return self.title


class Comments(models.Model):
	article = models.ForeignKey(Articles)
	text = models.TextField()
	writer = models.CharField(max_length=150)
# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	email = models.CharField(max_length=200,blank=True, null=True)
	text = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name