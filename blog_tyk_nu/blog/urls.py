from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from .views import BlogPostList, BlogPostDetail

urlpatterns = [
    ### admin site
    url(r'^%s/' % settings.ADMIN_PREFIX, include(admin.site.urls)),
    
    ### blog
    url(r'^blog/(?P<slug>[\w-]+)/$', BlogPostDetail.as_view(), name='blogpost_detail'),
    url(r'^$', BlogPostList.as_view(), name='frontpage'),

    ### tags
    url(r'^tags/(?P<slug>[\w-]+)/$', 'blog.views.tag_lookup', name='tag_lookup'),
    
    ### static pages
    url(r'^about/$', TemplateView.as_view(template_name="static/about_me.html"), name='about_me'),
    url(r'^contact/$', TemplateView.as_view(template_name="static/contact.html"), name='contact'),
    
    ### search
    url(r'^search/', include('haystack.urls')),
]
