from django import forms
from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']
        help_texts = {'username':''}
        
class ProfileForm(forms.ModelForm): 
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['username']
        
class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = '__all__'
        exclude = ['username', 'slno']