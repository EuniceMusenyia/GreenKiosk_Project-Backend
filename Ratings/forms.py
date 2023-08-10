from django import forms
from .models import Rating


class RatingUploadForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = "__all__"

        