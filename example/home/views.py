from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse 
from .models import Post, Comment, Post
from .forms import CommentForm, PostForm


#TODO Up for removal
#TODO We currently have no formal definition of a post ~ Thoth Gunter
def index(request):
    #TODO should we have different paths for guest and users.
    post_list = Post.objects.filter(author=request.user.id).order_by('-created_on')
    post_form = PostForm()


    if request.method == 'POST':
        new_post = PostForm(data=request.POST)
        if new_post.is_valid():
            new_post = new_post.save(commit=False)
            new_post.author = request.user
            new_post.save()
        else:
            #TODO remove once we have a better understanding of things
            print("!!!!!!!!!!!!!!!!!!ERROR!!!!!!!!!!!!!!!!")


    return render(request, 'dashboard/index.html', {'post_list': post_list, 'post_form': post_form})

def home(request):
    post_list = Post.objects.filter(public=True).order_by('-created_on')
    print("# of post", len(post_list))


    return render(request, 'home/index.html', {'post_list': post_list})


def register(request):
    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {"form": UserCreationForm}
        )
    elif request.method == "POST": 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("index"))



def post_detail(request, _slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=_slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method =='POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

