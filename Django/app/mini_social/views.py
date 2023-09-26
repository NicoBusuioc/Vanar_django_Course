from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.shortcuts import render, redirect

from datetime import date

year = date.today().year

def homePage(request):

  #check if 'bannerViewd' is in action
  bannerViewed = request.session.get('bannerViewed', False)
  sessionViews = request.session.get('viewsPerSession', 0)

  # mark the 'bannerViewd' to True inside the session
  request.session['bannerViewed'] = True
  request.session['viewsPerSession'] = sessionViews + 1

  template = loader.get_template('home.html')
  return HttpResponse(template.render({
                                      'message': "Welcome to our mini social network",
                                      'year': year,
                                      'bannerViewed': bannerViewed,
                                      'viewsPerSession': sessionViews
                                      }))




###
# There are 3 ways to call a WebPage, the last one is most used
##
def signInPage(request):
  signIn_dict = {'year': year}
  #messages.success(request, "Welcome, try to login.")
############################################################__1
  # template = loader.get_template('signin.html')
  # content = template.render(signIn_dict, request)
  # return HttpResponse(content)
############################################################__2
  # content = loader.render_to_string('signin.html', signIn_dict, request)
  # return HttpResponse(content)
############################################################__3
  return render(request, 'signin.html', signIn_dict)


def signInAction(request):
  correctUsername = "nicu"
  correctPassword = "123"
  
  #get values from the form
  inputUsername = request.GET['username']
  inputPassword = request.GET['password']

  if correctUsername == inputUsername and correctPassword == inputPassword:
    return HttpResponse("OK") #TODO: Go to User-Main Page

  messages.error(request, "Wrong Credentials, try again.")
  # return HttpResponseRedirect("/user/signin")
  return redirect("/user/signin")


def signUpPage(request):
  template = loader.get_template('signup.html')
  return HttpResponse(template.render({'year': year}))