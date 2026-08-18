from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.http import HttpResponseForbidden
def article_list(request):
   articles = Article.objects.all().order_by("-created_at")
   return render(request, "blog/article_list.html", {"articles": articles})

def article_detail(request, slug):
   article = get_object_or_404(Article, slug=slug)
   return render(request, "blog/article_detail.html", {"article": article})

@login_required
def article_create(request):
      form = ArticleForm(request.POST or None, request.FILES or None)
      if request.method == "POST" and form.is_valid():
         article = form.save(commit=False)
         article.author = request.user
         article.save()
         return redirect("article_detail", slug=article.slug)
      return render(request, "blog/article_form.html", {"form": form})
#from django.http import HttpResponseForbidden
@login_required
def article_edit(request, slug):
   article = get_object_or_404(Article, slug=slug)
   if article.author != request.user:
       return HttpResponseForbidden("Ruxsat yo‘q")
   form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
   if request.method == "POST" and form.is_valid():
       form.save()
       return redirect("article_detail", slug=article.slug)
   return render(request, "blog/article_form.html", {"form": form})


@login_required
def article_delete(request, slug):
   article = get_object_or_404(Article, slug=slug)

   if article.author != request.user:
       return HttpResponseForbidden("Ruxsat yo‘q")

   if request.method == "POST":
       article.delete()
       return redirect("article_list")
   return render(request, "blog/article_confirm_delete.html", {"article": article})


