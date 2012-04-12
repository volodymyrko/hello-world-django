# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.http import Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from contact.models import Contact
from contact.forms import ContactForm

FORM_SPLIT_BY = 5


def index(request):
    """ index page: show contacts
    """
    query = Contact.objects.all()[:1]
    if query:
        contact = query.get()
    else:
        raise Http404
    return render_to_response('index.html', {'contact': contact},
        context_instance=RequestContext(request))


@login_required()
def edit(request):
    contact = Contact.objects.all()[:1].get()
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
    else:
        form = ContactForm(instance=contact)
        #import pdb; pdb.set_trace()
    return render_to_response('edit.html', {'form': form,
        'number': FORM_SPLIT_BY}, context_instance=RequestContext(request))
