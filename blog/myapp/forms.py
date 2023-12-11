from .models import posts
from django.forms import ModelForm


class blog(ModelForm):
    class Meta:
        model = posts
        fields = '__all__'
