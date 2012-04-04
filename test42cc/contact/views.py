# Create your views here.
from django.shortcuts import render_to_response
from django.http import Http404
from contact.models import Contact

def index(request):
    #import pdb; pdb.set_trace()
    query = Contact.objects.all()[:1]
    if query:
        contact = query.get()
    else:
        raise Http404
    return render_to_response('index.html', {'contact': contact})