from django import forms
from .models import Teacher

class AddTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ("name",'phone','address','age','gender')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
           'phone': forms.NumberInput(attrs={'class': 'form-control'}),
           'address': forms.TextInput(attrs={'class': 'form-control'}),
            'age' : forms.NumberInput(attrs={'class': 'form-control'}),
            'render': forms.TextInput(attrs={'class': 'form-control'}),
       }
