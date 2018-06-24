from django.urls import path,re_path
from . import views as core_views

urlpatterns = [
    path('signup/',core_views.signup,name='signup'),
   ]