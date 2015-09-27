from django.views.generic import ListView, DetailView
from .models import BlogPost


class BlogPostList(ListView):
    queryset = BlogPost.objects.all()
    paginate_by = 25


class BlogPostDetail(DetailView):
    model = BlogPost


