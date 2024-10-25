from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:medicine_name>/", views.detail, name="detail")
]