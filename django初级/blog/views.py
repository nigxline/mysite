from django.contrib import auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from blog.models import Post, BlogRoll, BgRecord, Comment, WordsOfQiu

# Create your views here.
def home(request):
    post_list = Post.objects.all()
    hot_post_list = Post.objects.all().order_by('-page_view')[:5]
    recent_post_list = Post.objects.all()[:5]
    bgrecord_list = BgRecord.objects.all()
    blogroll_list = BlogRoll.objects.all()
    words_qiu = WordsOfQiu.objects.all()[0]

    paginator = Paginator(post_list, 2)
    page_num = request.GET.get('page_num', 1)
    page = paginator.page(int(page_num))

    context = {
        'post_list': post_list,
        'hot_post_list': hot_post_list,
        'recent_post_list': recent_post_list,
        'bgrecord_list': bgrecord_list,
        'blogroll_list': blogroll_list,
        'page': page,
        'words_qiu': words_qiu,
    }
    return render(request, 'blog/home.html', context)

def article(request):
    if request.method == 'GET':
        return render(request, 'blog/article.html')


def about(request):
    if request.method == 'GET':
        comment_list = Comment.objects.all()
        return render(request, 'blog/about.html', {'comment_list': comment_list})
    if request.method == 'POST':
        user = '测试'
        comment = request.POST.get('editorContent')

        Comment.objects.create(
            user=user,
            comment=comment,
        )
    return redirect(reverse('blog:about'))

def timeline(request):
    if request.method == 'GET':
        return render(request, 'blog/timeline.html')

def resource(request):
    if request.method == 'GET':
        return render(request, 'blog/resource.html')

def detail(request, pk):
    if request.method == 'GET':
        return redirect()

