import re

import markdown
from markdown.extensions.toc import TocExtension
from .models import Post, Category, Tag
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from django.views.generic import ListView, DetailView
import django.core.paginator


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        """
        覆写 get 原因: 为了获取 self.object 属性, 完成
                阅读量统计 +1 的功能.
        先调用 super().get 原因: 只有 get 方法被调用后, 
                才有self.object 属性, self.object 即 
                Post 的实例 post.  
        """
        response = super().get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        """
        覆写 get_object 方法的目的： 需要对 post.body 值进行渲染. 
        """
        post = super().get_object(queryset=None)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify=slugify),
        ])
            
        post.body = md.convert(post.body)

        m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
        post.toc = m.group(1) if m is not None else ''
        return post


class ArchiveView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        year = self.kwargs.get("year")
        month = self.kwargs.get("month")
        return super().get_queryset().filter(created_time__year=year,
                                             created_time__month=month)


class CategoryView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(category=cate)


class TagView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        t = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tag=t)



    