from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from .views import BlogPostList, BlogPostDetail, tag_lookup

urlpatterns = [
    ### admin site
    path(f"{settings.ADMIN_PREFIX}/", admin.site.urls),

    ### blog
    path('blog/<slug:slug>/', BlogPostDetail.as_view(), name='blogpost_detail'),
    path('', BlogPostList.as_view(), name='frontpage'),

    ### tags
    path('tags/<slug:slug>/', tag_lookup, name='tag_lookup'),

    ### static pages
    path('about/', TemplateView.as_view(template_name="static/about_me.html"), name='about_me'),
    path('contact/', TemplateView.as_view(template_name="static/contact.html"), name='contact'),
]
