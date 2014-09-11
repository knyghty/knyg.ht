from .models import Page


def nav(request):
    return {'nodes': Page.objects.all()}
