from django import forms
from first_app.models import Crypt

class NewUser(forms.ModelForm):
    class Meta():
        model = Crypt
        fields = '__all__'
