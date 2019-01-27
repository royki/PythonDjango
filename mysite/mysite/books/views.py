# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render_to_response
from mysite.books.models import Book, Author, Publisher
from django.core.mail import send_mail

# Create your views here.

def search_form(request):
	return render_to_response('search_form.html')


# def search(request):
# 	if 'q' in request.GET: # and request.GET['q']:
# 		q = request.GET['q']
# 		if not q:
# 			error = True
# 		else:
# 			books = Book.objects.filter(title__icontains=q)
# 			return render_to_response('search_results.html', {'books': books, 'query': q})
# 	# else:
# 		# return HttpResponse('Please submit a book title')
# 	return render_to_response('search_form.html', {'error': error})


def search(request):
	# error = False
	error = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			# error = True
			error.append('Enter a search term')
		elif len(q) > 20:
			# error = True
			error.append('Please submit a search with less than 20 characters')
		else:
			books = Book.objects.filter(title__icontains=q)
			return render_to_response('search_results.html', {'books': books, 'query': q})
	return render_to_response('search_form.html', {'error': error})

def author_list(request):
	authors = Author.objects.all()
	books = Book.objects.all()

	# Accessing ManyToMany Values
	b1 = Book.objects.get(id=3)
	b1.authors.all
	# Accessing ManyToMany Values in reverse
	a = Author.objects.get(first_name='Rabi')
	a.book_set.all()

	# Accessing foreign Key Values
	# b1.publishers.website # Put it in the template
	# Accessing foreign Key in reverse
	p = Publisher.objects.get(name='Desh')
	p.book_set.all()
	return render_to_response('author_list.html', {'authors': authors, 'books': books, 'a':a, 'b1':b1, 'p':p})
