from django.shortcuts import render
from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string

import random



def home_view(request, *args, **kwargs):

    random_id = random.randint(1, 4)

    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()
    print(id)


    context = {
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
        "object_list": article_queryset,
    }


    return render(request, "home_view.html", context)
