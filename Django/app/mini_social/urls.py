from django.contrib import admin
from django.urls import path
from mini_social.views import *



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', homePage),
    path('user/signin', signInPage),
    path('user/signup', signUpPage),
]
