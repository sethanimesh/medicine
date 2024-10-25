from django.contrib import admin

from medicine.models import Medicine, UserMedication

# Register your models here.
admin.site.register(Medicine)
admin.site.register(UserMedication)