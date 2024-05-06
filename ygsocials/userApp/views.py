from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .forms import SignUpForm, User_form, Admin_form, UserProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import messages
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect



# Create your views here.
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url  = reverse_lazy("login")
    template_name = 'registration/signup.html'

@login_required
def my_account(request, userid):
    profile = UserProfile.objects.all().filter(user_id = userid)
    # print(profile)
    return render(request=request, template_name='userApp/my_account.html', context={"userprofile":profile})