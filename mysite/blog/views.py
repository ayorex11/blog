from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def RegisterPage(request):
    form=CreateUserForm()
    if request.method == 'POST':
         form= CreateUserForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('blog:post_list',)
    context={'form': form}
    return render(request, 'register.html', context)
def post_list(request):
    
    object_list= Post.published.all()
    paginator= Paginator(object_list, 3)
    page= request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
        
    return render(request,
                  'list.html',
                  {'page':page,
                   'posts':posts})
        
    
def post_detail(request, year, month, day, post):
    post= get_object_or_404(Post, slug=post,
                            status='published',
                            date__year=year,
                            date__month= month,
                            date__day= day,)
    if request.method == 'POST':
        form= CommentForm(request.POST)
        
        if form.is_valid():
            comment= form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('blog:post_list', slug= post.slug)
    else:
        form= CommentForm()
    return render(request,
                  'detail.html',
                  {'post':post,
                   'form':form})
def createpost(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                post.title= request.POST.get('title')
                post.body= request.POST.get('content')
                post.author= request.POST.get('author_name')
                post.slug= post.title.lower().replace(" ", "-")
                post.save()
                
                return redirect('blog:post_list')
            else:
                pass
        return render(request,'create.html')
