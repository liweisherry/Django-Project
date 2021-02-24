from django.shortcuts import render, HttpResponse, redirect
from app01 import models

def login(request):
    if request.method == 'POST':
        #获取用户名和密码
        user = request.POST.get('user')
        pwd= request.POST.get('pwd')
        if models.User.objects.filter(username=user,password=pwd):
            return redirect('/index/')
    
    return render(request,'login.html')

def index(request):
    
    ret = models.User.objects.all()
    #ret = models.User.objects.get( password='123') #only allow to return one record
    ret = models.User.objects.filter( password='123')#return multiple record
    return render(request,'index.html')