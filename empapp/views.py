from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from .forms import *

def home(request):
    return render(request,'home.html')

def navbar(request):
    return render(request,'navbar.html')

def addemp(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        salary=int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        role = int(request.POST['role'])
        dept = int(request.POST['dept'])
        newemp=employee(firstname=firstname,lastname=lastname,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hiredate=datetime.now())
        newemp.save()
        # return HttpResponse('employee added successfully')
        return redirect(allemp)

    elif request.method=='GET':
        return render(request,'addemp.html')
    else:
        return HttpResponse('employee is not added')




def allemp(request):
    emp=employee.objects.all()
    return render(request,'allemp.html',{'emp':emp})





def removeemp(request,id=0):
    if id:
        try:
            empremove=employee.objects.get(id=id)
            empremove.delete()
            return redirect(removesuccess)
        except:
            return HttpResponse("Please select a valid employee")
    emp=employee.objects.all()
    return render(request,'removeemp.html',{'emp':emp})





def filteremp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emp=employee.objects.all()
        if name:
            emp=emp.filter(Q(firstname__icontains=name) | Q(lastname__icontains=name))
        if dept:
            emp=emp.filter(dept__name__icontains=dept)
        if role:
            emp = emp.filter(role__name__icontains=role)
        return render(request,'allemp.html',{'emp':emp})
    elif request.method=='GET':
        return render(request,'filteremp.html')
    else:
        return HttpResponse('an exception occured')






def login(request):
    if request.method == 'POST':
        a = loginform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            cd = a.cleaned_data['code']
            if em == "manager@gmail.com" and cd == 33355:
                    return redirect(home)
            else:
                return redirect(failed)
        else:
            return HttpResponse("not valid")
    else:
        return render(request, 'login.html')





def failed(request):
    return render(request,'failed.html')



def removesuccess(request):
    return render(request,'removesuccess.html')



def index(request):
    return render(request,'index.html')