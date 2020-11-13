from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

@method_decorator(login_required,name="dispatch")
class Index(View):
    def get(self,req):
        return render(req, 'index.html', {'name': req.user.first_name})
    def post(self,req):
        return HttpResponse("Post Req")

class LoginView(View):
    def get(self,req):
        return render(req,"login.html")
    def post(self,req):
        username=req.POST.get('u')
        password=req.POST.get('p')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(req,user)
            return redirect('/')
        else:
            return redirect('/')

class RegisterView(View):
    def get(self,req):
        return render(req,'register.html')
    def post(self,req):
        username = req.POST.get('username')
        password = req.POST.get('password')
        firstname = req.POST.get('firstname')
        lastname = req.POST.get('lastname')
        email = req.POST.get('email')
        user = User.objects.create_user(first_name = firstname, last_name = lastname, email = email, username=username, password=password)
        user.save()
        return redirect('/')

class LogoutView(View):
    def get(self,req):
        logout(req)
        return redirect("/login")