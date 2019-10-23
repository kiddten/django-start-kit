from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Article


def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:10]
    return render(request, 'subapp/list.html', {'latest_article_list': latest_article_list})


def detail(request, article_id):
    try:
        item = Article.objects.get(id=article_id)
    except Exception:
        raise Http404('Not found!')

    latest_comments_list = item.comment_set.order_by('-id')[:10]

    return render(request, 'subapp/detail.html', {'article': item, 'latest_comments_list': latest_comments_list})


def leave_comment(request, article_id):
    try:
        item = Article.objects.get(id=article_id)
    except Exception:
        raise Http404('Not found!')

    item.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('subapp:detail', args=(item.id,)))


def test(request):
    return HttpResponse('test-view')
