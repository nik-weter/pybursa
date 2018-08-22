from django import forms

from .models import Coache

#from coaches.models import Coache

class CoacheForm(forms.ModelForm):

    class Meta:
        model = Coache
        fields = ('name', 'surname', 'email', 'role', 'user', 'dossier')

 # widgets = {
        #     'role': forms.RadioSelect
        # }