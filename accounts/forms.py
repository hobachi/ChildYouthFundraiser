from django import forms


class RegistrationForm(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    login = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        login = self.cleaned_data.get('login')
        if login != password:
            raise forms.ValidationError({
                'login': 'Passwords mismatched'
            })
        return self.cleaned_data
