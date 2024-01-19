from django import forms

from app.models import *



class Stateform(forms.ModelForm):
    class Meta():
        model=State
        fields='__all__'


class Capitalform(forms.ModelForm):
    class Meta():
        model=Capital
        fields='__all__'
        #exclude=['Cno']
        #labels={'Sname':'SN'}
        #widgets={'Population':forms.PasswordInput}
