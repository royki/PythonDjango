# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	website = models.URLField()

	# def __unicode__(self): # change __str__ for python3
	def __str__(self):
		return self.name

class Author(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(blank=True, verbose_name='e-mail')

	def __str__(self):
		return u'%s %s' %(self.first_name, self.last_name)

class BookManager(models.Manager):
	def title_count(self, keyword):
		return self.filter(title__icontains=keyword).count()

class Book(models.Model):
	title = models.CharField(max_length=50)
	authors = models.ManyToManyField(Author)
	publishers = models.ForeignKey(Publisher)
	publication_date = models.DateField(blank=True, null=True)
	num_pages = models.IntegerField(blank=True, null=True)
	book_objects = BookManager()

	def __str__(self):
		return u'%s %s' %(self.title, self.authors)