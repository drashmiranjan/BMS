from django.shortcuts import render
from app.forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
import random
# Create your views here.
def home(request):
    un = request.session.get('username')
    if un:
        all_budget = Budget.objects.all()
        d = {'all_budget':all_budget}
        return render(request,'home.html',d)
    return render(request,'home.html')

def register(request):
    EUFO = UserForm()
    EPFO = ProfileForm()
    d = {'EUFO':EUFO, 'EPFO':EPFO}
    if request.method == 'POST' and request.FILES:
        UFO = UserForm(request.POST)
        PFO = ProfileForm(request.POST, request.FILES)
        if UFO.is_valid() and PFO.is_valid():
            pw = UFO.cleaned_data.get('password')
            MUFO = UFO.save(commit=False)
            MUFO.set_password(pw)
            MUFO.save()
            
            MPFO = PFO.save(commit=False)
            MPFO.username = MUFO
            MPFO.save()
            
            un = UFO.cleaned_data.get("username")
            message = f'''
            Dear {un},

We are thrilled to welcome you to BMS! 🎉

Thank you for registering with us. You are now part of a growing community dedicated to track the Expense

Here’s what you can do next:
✅ Explore our platform and discover exciting features.
✅ Complete your profile to make the most of our services.
✅ Stay connected with us for the latest updates and exclusive content.

If you have any questions, feel free to reach out to us at drashmiranjan36@gmail.com. We are always here to help!

Welcome aboard, and we look forward to an amazing journey together.

Best regards,
BMS Teams,
BMS
            '''
            email = UFO.cleaned_data.get('email')
            send_mail(
                'Welcome to Our BMS Track your Expenses',
                message,
                'drashmiranjan36@gmail.com',
                [email],
                fail_silently=False
            )
            return HttpResponseRedirect(reverse('home'))
    return render(request,'register.html',d)

def user_login(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        email = request.POST.get('email')
        pw = request.POST.get('password')
        AUO = authenticate(username = un, password = pw, email = email)
        if AUO:
            login(request,AUO)
            request.session['username'] = un
            request.session['pw'] = pw
            request.session['email'] = email
            otp = random.randint(1000,9999)
            request.session['otp'] = str(otp)
            
            message = f"Your OTP for verification is: {otp}. It is valid for 5 minutes."
            email = request.session.get('email')
            send_mail(
                'Welcome to Our BMS Track your Expenses | Get your OTP',
                message,
                'drashmiranjan36@gmail.com',
                [email],
                fail_silently=False
            )
            return HttpResponseRedirect(reverse('otp'))
        else:
            return HttpResponse('invalid Details')
    return render(request,'login.html')

def otp(request):
    if request.method == 'POST':
        otp1 = request.POST.get('otp')
        votp = request.session.get('otp')
        if otp1 == votp:
            return HttpResponseRedirect(reverse('home'))
    return render(request,'otp.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def profile(request):
    un = request.session.get('username')
    if un:
        UO = User.objects.get(username = un)
        PO = Profile.objects.get(username = UO)
        d = {'UO':UO , 'PO':PO}
        return render(request,'profile.html',d)
    return HttpResponseRedirect(reverse('user_login'))

def createbudget(request):
    un = request.session.get('username')
    if un:
        EBO = BudgetForm()
        d = {'EBO':EBO}
        if request.method == 'POST':
            UO = User.objects.get(username=un)
            BFO = BudgetForm(request.POST)
            MBFO = BFO.save(commit=False)
            MBFO.username = UO
            MBFO.save()
            return HttpResponseRedirect(reverse('home'))
        return render(request,'createbudget.html',d)
    return HttpResponseRedirect(reverse('user_login'))
    
def updatebudget(request, pk):
    Bobj = Budget.objects.get(pk=pk)
    d = {'Bobj':Bobj}
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        amount = request.POST.get('amount')
        
        Bobj.title = title
        Bobj.desc = desc
        Bobj.amount = amount
        Bobj.save()
        return HttpResponseRedirect(reverse('home'))
    return render(request,'updatebudget.html',d)

def deletebudget(request, pk):
    BOBJ = Budget.objects.get(pk=pk)
    BOBJ.delete()
    return HttpResponseRedirect(reverse('home'))
