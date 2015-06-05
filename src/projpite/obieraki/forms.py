from django import forms            
from django.contrib.auth.models import User   # fill in custom user info then save it 
from django.contrib.auth.forms import UserCreationForm      

class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Login:", max_length=30)
    password1 = forms.CharField(label="Haslo:", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Powtorz haslo:", widget=forms.PasswordInput())
    email = forms.EmailField(label="Email:", required = True)
    name = forms.CharField(label="Imie:", required = True)
    surname = forms.CharField(label="Nazwisko:", required = True)


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')        

    def save(self,commit = True):   
        user = super(RegisterForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['name']
        user.last_name = self.cleaned_data['surname']

        if commit:
            user.save()

        return user
