from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

class User_form(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]
    
class Admin_form(forms.ModelForm):
    genders = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('I had rather not say', 'I had rather not say'),
        ('LGBTQ', 'LGBTQ'),
        ('Others', ('Others')),
    ]

    profile_view_image = forms.ImageField(required=False, label='Dashboard Image')
    follower = forms.ChoiceField(choices=followers, required=False)
    gender = forms.ChoiceField(choices=genders, required=False, widget=forms.RadioSelect)
    
    class Meta:
        model = UserProfile
        fields = [
            'phone_number',
            'address',
            'gender',
            'date_of_birth',
            'followers',
            'country',
            'social_media',
            'profile_view',

            
        ]

        widgets = {
            'date_of_birth': forms.NumberInput(attrs={'type':'data'}),
        }


class UserProfileForm(forms.ModelForm):
    genders = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('I had rather not say', 'I had rather not say'),
        ('LGBTQ', 'LGBTQ'),
        ('Others', ('Others')),
    ]

    gender = forms.ChoiceField(choices= genders, required=False, widget=forms.RadioSelect )
    profile_view_image = forms.FileField(required=False, label='Profile viex Image')
    follower = forms.ChoiceField(choices=followers, required=False)


    class Meta:
        model = UserProfile
        fields = [
            'phone_number',
            'address',
            'gender',
            'date_of_birth',
            'followers',
            'country',
            'profile_view',
        ]

        widgets = {
                    'date_of_birth': forms.NumberInput(attrs={'type':'date'}),
            }



