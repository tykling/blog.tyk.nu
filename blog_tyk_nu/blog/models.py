from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(published=True)

class BlogPost(models.Model):
    allobjects = models.Manager()
    objects = PublishedManager()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(blank=True)
    published = models.BooleanField(default=True)
    tags = TaggableManager()

    class Meta:
        ordering = ['-created_date']

    def __unicode__(self):
        return unicode(self.title)

    def get_absolute_url(self):
        return reverse('blogpost_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        ### set/update slug
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

