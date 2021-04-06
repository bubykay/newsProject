from django.shortcuts import render
from .models import ScrapedNews
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):
    content1 = ScrapedNews.objects.exclude(body__isnull=True).order_by('-pk')

    page = request.GET.get('page', 1)
    paginator = Paginator(content1, 20)
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)
    except EmptyPage:
        content = paginator.page(paginator.num_pages)


    context = {
        'content': content,
        'description': 'Kokoroyin your number 1 news aggregator.',
        'keywords': 'News, Nigeria,',
        'title': 'Nigeria best news aggregator',
  
    }
    return render(request, 'index.html', context)

def news(request, slug):
    content = ScrapedNews.objects.get(slug=slug)
    content.views += 1
    trends = ScrapedNews.objects.order_by('-pk').order_by('-views')[:5]
    also = ScrapedNews.objects.order_by('-pk')[:25]
    content.save()
    context = {
        'content':content,
        'trends': trends,
        'also': also
    }
    return render(request, 'news_page.html', context )
