# Create your views here.
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from utils42cc.models import HttpRequestEntry

RECORDS_PER_PAGE = 10


def requests(request):
    """show last 10 saved http requests
    """
    all_request = HttpRequestEntry.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_request, RECORDS_PER_PAGE)
    try:
        requests = paginator.page(page)
    except EmptyPage:
        requests = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        requests = paginator.page(1)
    return render_to_response('requests.html', {'requests': requests},
        context_instance=RequestContext(request))
