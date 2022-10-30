from django.shortcuts import render

from articles.models import Article, Scope


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    news = Article.objects.all()
    
    context = {
        'object_list': news,
        'ordering': ordering,
    }

    
    return render(request, template, context)
