from django.contrib import admin

# Register your models here.
from .models import Team, Member

admin.site.register([Team, Member])