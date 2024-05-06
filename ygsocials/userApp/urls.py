from django.urls import path
from ygsocials.userApp import views as userViews
from views import *

# ====================
urlpatterns = [
    path("my_account/<int:userid>/", my_account, name="my_account"),
    
    ]
