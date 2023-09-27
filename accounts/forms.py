from django import forms
from .models import Account, UserProfile
import re
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
# from captcha.widgets import ReCaptchaV2Invisible




class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password'
    }))
    confirm_password = forms.CharField(min_length=8,  widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    first_name = forms.CharField(min_length=4, widget=forms.TextInput(attrs={
        'placeholder': 'First Name', 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '
    }))

    last_name = forms.CharField(min_length=4, widget=forms.TextInput(attrs={
        'placeholder': 'Last Name', 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '
    }))

    phone_number = forms.CharField(max_length=14, min_length=8, widget=forms.TextInput(attrs={
        'placeholder': 'phone_number'
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'email'
    }))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    # captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)
        


    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email' ,'password']

    

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not Match!"
            )     

        
    def clean(self):
            cleaned_data = super(RegistrationForm, self).clean()
            password = cleaned_data.get('password')
            if not re.findall("/d", password):
                raise ValidationError(
                    _("The password must contain at least 1 digit, 0-9."),
                    code='password_no_number',
                )
        
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("The password must contain at least 1 uppercase letter, A-Z."),
                code='password_no_upper',
            )

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        if not re.findall('[a-z]', password):
            raise ValidationError(
                _("The password must contain at least 1 lowercase letter, a-z."),
                code='password_no_lower',
            )
            
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("The password must contain at least 1 symbol: " +
                "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )
        


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='Enter First name'
        self.fields['last_name'].widget.attrs['placeholder']='Enter Last name'
        self.fields['phone_number'].widget.attrs['placeholder']='Enter Phone number'
        self.fields['email'].widget.attrs['placeholder']='Enter Email'
        self.fields['password'].widget.attrs['placeholder']='Enter Password'
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

    

    

        

class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_number')
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

    


class UserProfileFrom(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, error_messages= {'invalid':("image files only!")}, widget=forms.FileInput)
    class Meta:
        model = UserProfile
        fields = ('address_line_1', 'address_line_2', 'city', 'state', 'country', 'profile_picture')

    def __init__(self, *args, **kwargs):
        super(UserProfileFrom, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'



    





