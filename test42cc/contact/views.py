# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.http import Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.http import HttpResponse
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


@login_required(login_url='/admin/')
def edit(request):
    contact = Contact.objects.all()[:1].get()
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            if request.is_ajax():
                response = {'status': 'OK'}
                data = {'name': 'photo', 'value': contact.photo}
                response['image'] = form.fields['photo'].widget.render(**data)
                return HttpResponse(simplejson.dumps(response))
            return redirect(reverse('index'))
        else:
            if request.is_ajax():
                response = {'status': 'BAD'}
                errors = dict()
                for label_id, error in form.errors.items():
                    errors[label_id] = error
                response['errors'] = errors
                return HttpResponse(simplejson.dumps(response))
    else:
        form = ContactForm(instance=contact)
    return render_to_response('edit.html', {'form': form,
        'number': FORM_SPLIT_BY}, context_instance=RequestContext(request))
