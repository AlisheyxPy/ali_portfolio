from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Mode


class CreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Mode
        fields = ("username",'first_name','last_name','email','age','country')


class ChangeForm(UserChangeForm):
    class Meta(UserCreationForm):
        model = Mode
        fields = ("username",'first_name','last_name','email','age','country')