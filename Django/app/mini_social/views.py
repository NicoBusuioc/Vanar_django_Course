from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Post, CustomUser
from django.contrib.auth import authenticate, login, logout


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
  dict = {'year': year}
  #messages.success(request, "Welcome, try to login.")
############################################################__1
  # template = loader.get_template('signin.html')
  # content = template.render(dict, request)
  # return HttpResponse(content)
############################################################__2
  # content = loader.render_to_string('signin.html', dict, request)
  # return HttpResponse(content)
############################################################__3
  return render(request, 'signin.html', dict)


def signInAction(request):
  #get values from the form
  inputUsername = request.GET['username']
  inputPassword = request.GET['password']

  user = authenticate(request, username=inputUsername, password=inputPassword)

  if user is not None:
    login(request, user)
    return redirect("/user/profile")

  messages.error(request, "Wrong Credentials, try again.")
  # return HttpResponseRedirect("/user/signin")
  return redirect("/user/signin")

def signUpAction(request):
  inputUsername = request.GET['username']
  inputPassword = request.GET['password']
  inputEmail = request.GET['email']
  inputConfPassword= request.GET['confirm_password']

  #check data validity
  if inputPassword != inputConfPassword:
    messages.error(request, "Passwords do not match!")
    return redirect("/user/signup")
  #TODO check data validity 

  #create a new user with data
  c_user = CustomUser.objects.create_user(username=inputUsername, password=inputPassword, email=inputEmail)
  c_user.save()

  return redirect("/user/signin")


def signUpPage(request):
  dict = {'year': year}
  return render(request, 'signup.html', dict)


def createPost(request):
  # creating and saving post entity
  p = Post(title="My first Post", body="test!!!")
  p.save()

  return HttpResponse("Post saved")


def profilePage(request):
  dict = {
    'year': year,
    'user': request.user,
    }
  
  if request.user.is_authenticated:
    return render(request, 'profile.html', dict)
  else:
    return redirect("/user/signin")
  

def logOut(request):
  logout(request)
  return redirect("/user/signin")
