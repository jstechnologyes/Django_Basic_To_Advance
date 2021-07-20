from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash,get_user_model
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
UserModel=get_user_model()
# Create your views here.
def loginuser(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, "Successfully Login")
                return redirect('homeview')
            else:
                messages.error(request,'Inviled Username or Password')
        else:
            messages.error(request, 'Inviled Username or Password')
    else:
        form = AuthenticationForm()
    return render(request,'session/login.html',{'form':form})

def logoutuser(request):
    logout(request)
    messages.success(request, "Successfully Logout")
    return redirect('homeview')

from .forms import SignUpForm
def registration(request):
    if request.method == "POST":
        form= SignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active=False
            user.save()
            current_site=get_current_site(request)
            mail_subject='Active Your Account'
            message=render_to_string('session/account.html',{
                'user':user,
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })
            send_mail= form.cleaned_data.get('email')
            email= EmailMessage(mail_subject,message,to=[send_mail])
            email.send()
            messages.success(request,'Successfull Created Account')
            messages.info(request,'Activate Your account from the mail you provided')
            return redirect('login')
    else:
        form = SignUpForm
    return render(request,'session/signup.html',{'form':form})
def activate(request,uidb64,token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=UserModel._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,WindowsError):
        user=None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        messages.success(request,"Your accout is activated now, you can now login")
        return redirect('login')
    else:
        messages.warning(request,"activation link is invaild")
        return redirect('singup')

def change_password(request):
    if request.method=="POST":
        form= PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            update_session_auth_hash(request,form.user)
            messages.success(request,"Password Change Succefully")
            return redirect('homeview')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'session/change_pass.html',{'form':form})



