from django.shortcuts import render

# Create your views here.

from datetime import datetime
from blog.models import Article, Category

def hello_world(request):
	return render(request,"hello_world.html",{'current_time':datetime.now()})

def home(request):
	# get all the Article

	article_list = Article.objects.all()
	return render(request,"home.html",{'article_list':article_list})

def article_detail(request, id):
	article = Article.objects.get(id=id)
	return render(request, "article.html", {'article': article})