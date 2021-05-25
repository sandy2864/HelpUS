from django import forms
from .models import Upload,Image

class UploadForm(forms.ModelForm):
    class Meta:
        model=Image
        fields='__all__'
        labels={'image':"",'loc':"",'name':"",'address':"",'Desc':"",'need':"","map":"",'mob':""}
       

        name = forms.CharField(label='name', 
                    widget=forms.TextInput(attrs={'placeholder': 'Name'}))
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Name'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder': 'Address'}),
            'loc':forms.Select(attrs={'class':'form-control','placeholder': 'Select Area'}),
            'Desc':forms.TextInput(attrs={'class':'form-control','placeholder': 'Description'}),
            'need':forms.TextInput(attrs={'class':'form-control','placeholder': 'Need Category'}),
            'map':forms.TextInput(attrs={'class':'form-control','placeholder': 'Map Location'}),
            'mob':forms.TextInput(attrs={'class':'form-control','placeholder': 'Contact Number'}),

            # 'image':forms.ImageField(attrs={'class':'form-control'}),
            
        }
        