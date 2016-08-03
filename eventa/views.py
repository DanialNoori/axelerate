from django.shortcuts import render
from .models import Event
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def events_page(request):
	if request.method == "GET":
		events = Event.objects.all().order_by('date')
		paginator = Paginator(events, 7)
		page = request.GET.get('page')
		try:
			thisevents = paginator.page(page)
		except PageNotAnInteger:
			thisevents = paginator.page(1)
		except EmptyPage:
			thisevents = paginator.page(paginator.num_pages)

		return render(request, 'events.html', { 
			'events' : thisevents
			})