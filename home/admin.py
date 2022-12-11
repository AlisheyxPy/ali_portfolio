from django.contrib import admin
from .models import Mode
from .form import CreateForm,ChangeForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class Obshi(UserAdmin):
    add_form = CreateForm
    form = ChangeForm
    model = Mode
    list_display = ['email','first_name','last_name','username','age','country','is_staff']


admin.site.register(Mode)