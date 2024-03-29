from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Post, CustomUser
from django.contrib.auth import authenticate, login, logout
from random import randint
import time


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
  user = CustomUser.objects.get(pk=request.user.id)
  request.user = user
  dict = {
    'year': year,
    'user': user,
    }
  
  if request.user.is_authenticated:
    return render(request, 'profile.html', dict)
  else:
    return redirect("/user/signin")
  

def logOut(request):
  logout(request)
  return redirect("/user/signin")

def profileEditPage(request):
  dict = {
    'year': year,
    'user': request.user,
    }
  
  if request.user.is_authenticated:
    return render(request, 'profile-edit.html', dict)
  else:
    return redirect("/user/signin")
  
def profileSavAction(request):
  # create a local variable with user
  user = CustomUser.objects.get(pk=request.user.id)

  if request.FILES.get('avatar'):
    inputFileAvatar = request.FILES['avatar']
    avatarName = f"images/avatar{randint(1000, 9000)}-{time.time()}.png"
    user.avatar = avatarName  #save image name in order to read it later when rendering profile.html
    with open(f"./Django/app/mini_social/static/{avatarName}", "wb+") as f:
      for chunk in inputFileAvatar.chunks():
        f.write(chunk)
  else:
    pass   # No File was imported

  inputUsername = request.POST['username']
  inputEmail = request.POST['email']
  inputPassword = request.POST['password']
  inputConfPassword= request.POST['confirm_password']


  user.username = inputUsername
  user.email = inputEmail
  if inputPassword != "":
    if inputPassword == inputConfPassword:
      user.set_password(inputPassword)
    else:
      messages.error(request, "Passwords do not match!")
      return redirect("/user/signin") ## in case of error exit witthout saving
  
  user.save()
  return redirect("/user/signin")
