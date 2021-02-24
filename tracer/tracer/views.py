from django.shortcuts import render, HttpResponse, redirect


def login(request):
    if request.method == 'POST':
        #获取用户名和密码
        user = request.POST.get('user')
        pwd= request.POST.get('pwd')
        if user =='alex' and pwd =='123':
            return redirect('/index/')
    
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')


def template_test(request):
    name_list=['a','b','c']
    return render(request,'template_test.html',{'name_list':name_list})