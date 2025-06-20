from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User

from django.contrib.auth import get_user_model

User = get_user_model()
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'password1', 'password2']  # ✅ no 'username'


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'email', 'bio']
