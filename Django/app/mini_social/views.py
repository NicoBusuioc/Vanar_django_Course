from django.http import HttpResponse
from django.template import loader
from datetime import date

year = date.today().year

def homePage(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render({
                                      'message': "Welcome to our mini social network",
                                      'year': year
                                      }))

def signInPage(request):
  template = loader.get_template('signin.html')
  return HttpResponse(template.render({
                                      'year': year
                                      }))

def signUpPage(request):
  template = loader.get_template('signup.html')
  return HttpResponse(template.render({
                                      'year': year
                                      }))