from django.views.generic import View
from django.shortcuts import render
from .models import Blog
from django.http import JsonResponse


class IndexView(View):
    def get(self, request, *args, **kwargs):
        blog_data = Blog.objects.all()
        return render(request, 'app/index.html', {
            'blog_data': blog_data,
        })


class AddView(View):
    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        # テンプレートから送信されたtitleを取得
        # 送信ボタンが押されたらtitleを取得してデータベースに保存
        blog = Blog()
        blog.title = title
        blog.save()

        data = {
            'title': title,
        }
        return JsonResponse(data)


class SearchView(View):
    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        blog_data = Blog.objects.all()
        title_list = []

        if title:
            blog_data = blog_data.filter(title__icontains=title)

        for blog in blog_data:
            title_list.append(blog.title)
        
        data = {
            'title_list': title_list,
        }
        return JsonResponse(data)