from django.shortcuts import render
from .models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def news_main(request):
	if request.method == "GET":
		news = News.objects.all().order_by('-datePublished')
		paginator = Paginator(news, 7)
		page = request.GET.get('page')
		try:
			pagenews = paginator.page(page)
		except PageNotAnInteger:
			pagenews = paginator.page(1)
		except EmptyPage:
			pagenews = paginator.page(paginator.num_pages)

		return render(request, 'news.html', { 
			'news' : pagenews
			})

def news_page(request, slug, news_id):
	if request.method == 'GET':
		if News.objects.filter(id=news_id):
			news = News.objects.get(id=news_id)
			news.viewCount += 1
			news.save()
			return render(request, 'newspage.html', {
				'post' : news
				})
		else:
			error = 'No news Found'
			return HttpResponseRedirect("/news")