# Create your views here.
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
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


@login_required
def prio(request):
    """ change priority
    """
    good_actios = ['plus', 'minus']
    result = {'status': "BAD"}
    r_id = request.GET.get('id', '')
    action = request.GET.get('action', '')

    if action not in good_actios:
        return HttpResponse(simplejson.dumps(result))

    try:
        obj = HttpRequestEntry.objects.get(id=r_id)
    except:
        return HttpResponse(simplejson.dumps(result))

    if action == 'plus':
        obj.priority += 1
    elif action == 'minus':
        obj.priority -= 1
    obj.save()
    result = {'status': "OK", 'prio': obj.priority}

    return HttpResponse(simplejson.dumps(result))
