from django.shortcuts import render,redirect

from blog.models import Post


def AddPost(request):
    if request.method == "POST":
        print(request.POST)
        title = request.POST.get("title")
        content = request.POST.get("content")
        Post.objects.create(title=title, content=content, author=request.user)
        return redirect('blog:addpost')
    else:
        posts = Post.objects.all()
        context = {'posts': posts}
        return render(request,"addpost.html", context)