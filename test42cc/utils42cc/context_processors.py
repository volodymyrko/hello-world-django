from django.conf import settings


def django_settings(request):
    """add django.settings to the context
    """
    return {'django_settings': settings}
