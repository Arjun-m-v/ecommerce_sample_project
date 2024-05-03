from django.shortcuts import render,redirect
from django.views import View
from account.forms import RegForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.generic import CreateView,FormView,TemplateView
from django.urls import reverse_lazy

# Create your views here.

# class LandingView(View):
#     def get(self,request):
#         return render(request,"landing.html")
    
class LandingView(TemplateView):
    template_name="landing.html"
    

# class LoginView(View):
#     def get(self,request):
#         form=LoginForm()
#         return render(request,"login.html",{"form":form})
    
class LoginView(FormView):
    form_class=LoginForm
    template_name="login.html"
    def post(self,request):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get('username')
            pswd=form_data.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                return redirect("uhome")
        else:
            return render(request,"login.html",{"form":form_data})
    
# class RegisterView(View):
#     def get(self,request):
#         form=RegForm()
#         return render(request,"reg.html",{"form":form})
#     def post(self,request):
#         form_data=RegForm(data=request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             messages.success(request,"User Registration Successfull")
#             return redirect("login")
#         else:
#             messages.success(request,"User Registration Failed")            
#             return render(request,"reg.html",{"form":form_data})
           
class RegisterView(CreateView):
    form_class=RegForm
    template_name="reg.html"
    success_url=reverse_lazy("login")

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("log")