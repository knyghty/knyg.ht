from django.core.urlresolvers import reverse
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Page(MPTTModel):
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=64)
    url = models.CharField(max_length=255, blank=True, unique=True)
    icon = models.CharField(max_length=30)
    content = models.TextField()
    position = models.PositiveSmallIntegerField()
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children')

    class Meta:
        ordering = ('parent__position', 'position')

    class MPTTMeta:
        order_insertion_by = ['position']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.url:
            return reverse('page', args=(self.url,))
        else:
            return reverse('home')
