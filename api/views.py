from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core import serializers
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from api.models import Ticket

from django.template import RequestContext

def index(request):
    return render_to_response("index.html", context_instance=RequestContext(request))


class TicketsView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse(serializers.serialize("json", Ticket.objects.all()), mimetype='application/json')

    def post(self, request, *args, **kwargs):
        title = request.POST['title']
        description = request.POST['description']
        t = Ticket(title=title, description=description)
        t.save()
        data = serializers.serialize("json", [t])
        return HttpResponse(data, mimetype='application/json')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(TicketsView, self).dispatch(request, *args, **kwargs)