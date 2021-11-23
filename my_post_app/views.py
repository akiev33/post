from django.shortcuts import render, redirect, get_object_or_404

from my_post_app.forms import PostForm, MyPostModelForm, ImageForm
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



def create_post(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        description = request.POST.get('description')
        print(description)

        model = Post
        if name and description:
            model.objects.create(name=name, description=description)
            return redirect('post')

    return render(request, 'create_post.html', locals())


def new_create(request):
    form=PostForm()
    model = Post
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            model.objects.create(name=name, description=description)
            return redirect('post')


    return render(request, 'new_create.html', locals())


def model_form_post(request, pk):
    form = MyPostModelForm
    post = get_object_or_404(Post, id=pk)
    form = MyPostModelForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post')
    return render(request, 'model_form.html', locals())


def create_image(request):
    form = ImageForm
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post')
    return render(request, 'image.html', locals())



