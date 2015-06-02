from django import forms
class RegisterForm(forms.Form):
    username = forms.CharField(label="Login:",max_length=30)
    email = forms.EmailField(label="Email:")
    password1 = forms.CharField(label="Haslo:",widget=forms.PasswordInput())
    password2 = forms.CharField(label="Powtorz haslo:",widget=forms.PasswordInput())
    phone = forms.CharField(label="Telefon:",max_length=20,required=False)