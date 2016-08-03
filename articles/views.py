from django.shortcuts import render
from .models import Articles, Comments
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def blog_main(request):
	if request.method == "GET":
		articles = Articles.objects.all().order_by('-datePublished')
		paginator = Paginator(articles, 7)
		page = request.GET.get('page')
		try:
			pageArticles = paginator.page(page)
		except PageNotAnInteger:
			pageArticles = paginator.page(1)
		except EmptyPage:
			pageArticles = paginator.page(paginator.num_pages)

		return render(request, 'blog.html', { 
			'articles' : pageArticles
			})


def blog_page(request):
	if request.method == 'GET':
		return render(request, 'blog.html')

def main_page(request):
	if request.method == 'GET':
		return render(request, 'index.html')


from .forms import CommentForm
def post_page(request, slug, post_id):
	if request.method == 'GET':
		if Articles.objects.filter(id=post_id):
			post = Articles.objects.get(id=post_id)
			post.viewCount += 1
			post.save()
			comments = Comments.objects.filter(article= post)
			form = CommentForm()
			return render(request, 'post.html', {
				'post' : post, 'comments' : comments, 'form': form
				})
		else:
			error = 'No Articles Found'
			return HttpResponseRedirect("/blog")
	if request.method == 'POST':
		if Articles.objects.filter(id=post_id):
			post = Articles.objects.get(id=post_id)
			form = CommentForm(request.POST)
			comments = Comments.objects.filter(article= post)
			if form.is_valid():
				comment = Comments.objects.create(article=post, text=form.cleaned_data['text'],
					writer=form.cleaned_data['writer'])
				return HttpResponseRedirect('/blog/posts/' + post.id.__str__() + '/' + post.slug.__str__())

			else:
				return render(request, 'post.html', {
					'post' : post, 'comments' : comments , 'form' : form
					})

def about_us(request):
	if request.method == 'GET':
		return render(request, 'about.html')


from .models import Contact
def contact_us(request):
	if request.method == 'GET':
		return render(request, 'contact.html')
	if request.method == 'POST':
		Contact.objects.create(name=request.POST['name'],
			text=request.POST['text'],
			email=request.POST['email'],)
		return render(request, 'contact.html', 
			{
			'success' : '1'
			})


def become_writer(request):
	if request.method == 'GET':
		return render(request, 'becomewriter.html')

