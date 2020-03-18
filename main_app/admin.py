from django.contrib import admin
from .models import Finch, Feeding, Poop, Photo

# Register your models here.
admin.site.register(Finch)
admin.site.register(Feeding)
admin.site.register(Poop)
admin.site.register(Photo)