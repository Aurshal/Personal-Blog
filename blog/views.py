from django.shortcuts import render,get_object_or_404
from blog.models import Blog
# Create your views here.
def blog_page(request):
    blogs = Blog.objects.order_by('-created')[:4]
    context = {
        'blogs':blogs
    }
    return render(request,'blog/blog_page.html',context)

def blog_detail(request,blog_id):
    blog = get_object_or_404(Blog,pk = blog_id)
    context = {
        'blog':blog
    }
    return render(request,'blog/blog_detail.html',context)
