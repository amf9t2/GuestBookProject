from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.http import HttpResponse
from django.template import Template, Context
from GuestBookApp.models import Guests

def home(request):
    template = Template(
        """Hello, world! Here are all the records in my guest book world:
{% for guest in guestbook %}
{
    {guest.last_name}
}
{% endfor %}"""
    )

    guestbook = Guests.objects.all()
    context = Context({"guestbook": guestbook})

    return HttpResponse(template.render(context))