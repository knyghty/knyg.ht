from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Page


def home(request):
    page = get_object_or_404(Page, url='')
    return render(request, 'pages/page_detail.html', {'page': page})


class DetailView(generic.DetailView):
    model = Page
    slug_field = 'url'
    slug_url_kwarg = 'url'
