from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(u'Name', max_length=50)

	def __unicode__(self):
		return self.name

class Article(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	photo = models.URLField(blank=True)
	location = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey('Category', blank=True, null=True)

	def __unicode__(self):
		return self.title