from django.contrib.auth.models import Group
from . import forms
from django.shortcuts import render,redirect

from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'index.html')


def index(request):
    return render(request,'index.html')

def admin(request):
    return render(request,'admin.html')

def students(request):
    return render(request,'students.html')

def header(request):
    return render(request,'header.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')

def admin_signup_view(request):
    form=forms.AdminSignupForm()
    if request.method=='POST':
        form=forms.AdminSignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()

            my_admin_group=Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)

    return render(request,'admin_signup.html',{'form':form})

def student_signup_view(request):
    form1=forms.StudentUserForm()
    form2=forms.StudentExtraForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.StudentUserForm(request.POST)
        form2=forms.StudentExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            # user.set_password(user.password)
            # user.save()
            f2 = form2.save(commit=False)
            f2.user = user
            user2 = f2.save()

            #my_student_group = Group.objects.get_or_create(name='STUDENT')
            #my_student_group[0].user_set.add(user)

         #return HttpResponseRedirect('studentlogin')
    return render(request,'studentsignup.html',context=mydict)



