from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
import datetime


# Create your models here.
class News(models.Model):

	class Meta():
		verbose_name = 'News'
		verbose_name_plural = 'News'

	imageTitle = models.ImageField(upload_to='media/', blank=True, null=True)
	title = models.TextField()
	subtitle = models.TextField()
	content = RichTextUploadingField()
	datePublished = models.CharField(max_length=11, blank=True, null=True)
	viewCount = models.IntegerField(default=0)
	slug = models.SlugField(blank=True, null=True)


	def save(self, *args, **kwargs):
		self.slug = self.title.replace(' ', '-')
		self.datePublished = datetime.datetime.now()
		super(News, self).save(*args, **kwargs)


	def __str__(self):
		return self.title
