from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
def hello(request):
    user_list = User.objects.all()
    # user_list = Person.objects.all()
    return render(request, 'table.html', {'userArray': user_list})


def hi(request):
    # emp = Person()
    # emp.name = 'binbinbin'
    # emp.save()
    return render(request, 'basic/404.html')

    # def index(request):
    #     return render(request, '404.html')
