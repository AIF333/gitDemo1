from django.shortcuts import render
from . import  models


def main_page(request):
	articles=models.YtArticle.objects.all()
	return render(request,'ytblog/main_page.html',{'articles':articles})

def article_page(request,article_id):
	article=models.YtArticle.objects.get(pk=article_id)
	return render(request,'ytblog/article.html',{'article':article})

def edit_page(request,article_id):
	if str(article_id) == '0':
		return render(request, 'ytblog/edit_page.html')
	article=models.YtArticle.objects.get(pk=article_id)
	return render(request, 'ytblog/edit_page.html',{'article':article})


def edit_action(request):
	title=request.POST.get('title','文章标题-默认值')
	pubtime=request.POST.get('pubtime','2018')
	content=request.POST.get('content','文章内容-默认值')
	article_id=request.POST.get('article_id','0')

	if str(article_id) == '0':
		models.YtArticle.objects.create(title=title,pubtime=pubtime,content=content)
		articles=models.YtArticle.objects.all()
		return render(request,'ytblog/main_page.html',{'articles':articles})
	else:
		article=models.YtArticle.objects.get(pk=article_id)
		article.title=title
		article.pubtime=pubtime
		article.content=content
		article.save()
		return render(request, 'ytblog/article.html', {'article': article})
