from django.shortcuts import render, get_object_or_404
from blog.models import Post

# روش اول
# def blog_view(request,cat_name=None,author_username=None):
#     posts = Post.objects.filter(status=1)
#     if cat_name:
#         posts = posts.filter(category__name=cat_name)
#     if author_username:
#         posts = posts.filter(author__username = author_username)
#     context = {'posts':posts}
#     return render(request, 'blog/blog-home.html',context)

# روش دوم که روش بهتر و تمیزتری هست
def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request,pid):
    # برای بهینه کردن کوئری می تونیم از این روش پایین که در دوخط نوشته شده هم استفاده کنیم.
    # posts = Post.objects.filter(status=1)
    # post = get_object_or_404(posts,pk=pid, status=1)
    post = get_object_or_404(Post,pk=pid, status=1)
    context = {'post':post}
    return render(request, 'blog/blog-single.html', context)

def test(request):
    return render(request,'test.html')

def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)
