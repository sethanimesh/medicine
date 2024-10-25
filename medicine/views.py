from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from medicine.models import Medicine

# Create your views here.
def index(request):
    medicine_list = Medicine.objects.all()
    template = loader.get_template('medicine/index.html')
    context = {'medicine_list':medicine_list,}
    return HttpResponse(template.render(context, request))