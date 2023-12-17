from django.shortcuts import render
from django.views.generic.base import View
from .models import  Post


#Вывод записей
class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list' : posts})