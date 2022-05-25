from django import forms
from .models import User

class UserLogin(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length = 50, widget=forms.PasswordInput)

    class Meta:
        # model
        model = User

        # displaying fields
        fields = '__all__'

    # method for cleaning the data
    def clean(self):
        super(UserLogin, self).clean()

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        return self.cleaned_data