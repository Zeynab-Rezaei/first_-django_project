from django.shortcuts import render, get_object_or_404
from blog.models import Post

def blog_view(request):
    posts = Post.objects.filter(status=1)
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