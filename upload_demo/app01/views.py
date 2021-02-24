from django.shortcuts import render,reverse
from django.views import View
from django.http import HttpResponse


# Create your views here.


class Upload(View):
    def get(self, request):
        return render(request, 'upload.html')
    
    def post(self, request):
        print(request.POST)
        file = request.FILES.get('f1')
        print(file)
        with open(file.name, 'wb') as f:
            for i in file:
                f.write(i)
        return HttpResponse('ok')


def index(request):
   return render(request,'index.html')

def blogs(request,year,month):
    print(year,type(year))
    return render(request,'2020.html')
def blog(request):
    url=reverse('blog')
    print(url)
    return HttpResponse('blog')