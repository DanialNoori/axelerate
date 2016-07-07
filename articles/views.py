from django.shortcuts import render
from .models import Articles
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def blog_main(request):
	if request.method == "GET":
		articles = Articles.objects.all()
		paginator = Paginator(articles, 7)
		page = request.GET.get('page')
		try:
			pageArticles = paginator.page(page)
		except PageNotAnInteger:
			pageArticles = paginator.page(1)
		except EmptyPage:
			pageArticles = paginator.page(paginator.num_pages)

		return render(request, 'index.html', { 
			'articles' : pageArticles
			})


def blog_page(request):
	if request.method == 'GET':
		return render(request, 'blog.html')

def post_page(request, slug, post_id):
	if request.method == 'GET':
		post = Articles.objects.get(id=post_id)
		if post:
			return render(request, 'post.html', {
				'post' : post
				})
		else:
			error = 'No Articles Found'
			return render(request, 'post.html')