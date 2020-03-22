from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
import json

# Create your views here.

def home(request):
    return render(request,'home.html')


def register(request):
    return render(request,'register.html')


def saveuserregister(request):
    if request.method=="POST":
        name=request.POST['name']
        password=request.POST['pass1']
        confirmpassword=request.POST['pass2']
        mobile=request.POST['mobile']
        usertype=request.POST['type']
        email=request.POST['email']
        resume=request.FILES['file']
    return JsonResponse({'status':'success'})


def education(request):
    if request.method=="POST":
        print(request.POST)
        qualification=request.POST['edu']
        course=request.POST['course']
        specialization=request.POST['specialization']
        university=request.POST['uni']
        coursetype=request.POST['ctype']
        passingyear=request.POST['passout']
        skills=request.POST.getlist('skill[]')
    return JsonResponse({'status':'success'})


def experience(request):
    if request.method=="POST":
        designation=request.POST['Desc']
        company=request.POST['company']
        experience=request.POST['experience']
        annualsalary=request.POST['annualsal']
        workingsince=request.POST['fromdate']
        workingtill=request.POST['todate']
        noticeperiod=request.POST['notice']
        industry=request.POST['industry']
        role=request.POST['role']
        functionalarea=request.POST['area']
    return JsonResponse({'status':'success'})


def login(request):
    if request.method=="POST":
        name=request.form['name']
        password=request.form['password']
        response=requests.get("http://localhost:8001/login",json={'name':name,'password':password})
        data=response.json()
    return render(request,'login.html')


