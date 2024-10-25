from django.http import HttpResponse
from django.shortcuts import render

from medicine.models import Medicine

# Create your views here.
def index(request):
    medicine_list = Medicine.objects.all()
    return HttpResponse(medicine_list)