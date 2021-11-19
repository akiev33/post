from django.shortcuts import render, redirect, get_object_or_404
from my_post_app.models import Post


def get_post(request):
    posts = Post.objects.all()
    return render(request, 'all_post.html', locals())


def detail_post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'detail_post.html', locals())



def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return redirect('post')

