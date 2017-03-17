from django.contrib.auth.models import User
from django.shortcuts import render
from django import forms
from django.http import HttpResponse
import datetime
from hello.models import Person

class UserForm(forms.Form):
    name = forms.CharField()

def register(request):
    if "POST" == request.method:
        # form = UserForm(request.POST)
        # if form.is_valid():
        #     print(form.cleaned_data)
        #     return HttpResponse('ok')

        name = request.POST['name']
        sex = request.POST['sex']
        print(name)
        print(sex)

        Person.objects.create(
            name  = name,
            sex = sex
        )
        # Person.save()

        return HttpResponse("添加出版社信息成功")
        # pass
    else:
        # form = UserForm()
    # return HttpResponse('basic/register.html', {'form': form})
    #     print(form.name)
    #     return render(request, 'basic/register.html', {'form': form} )
        return render(request, 'basic/register.html' )

# Create your views here.
def hello(request):
    user_list = User.objects.all()
    # user_list = Person.objects.all()
    return render(request, 'table.html', {'userArray': user_list})

def index(request):
    # data_list = ("oneone", "two", "three")
    data_list = ["oneone", "two", "three"]
    datea = '2017-02-10'
    date1 = '2017-02-10'
    date2 = '2011-02-10'

    valuea = 'this is a string'


    print(data_list)
    return render(request, 'basic/index.html', locals())
    # return render(request, 'basic/index2.html', locals())
    # return render(request, 'basic/index.html',
    #               {'data_list': data_list,
    #                'date1':date1}
    #               )

def hi(request):
    # emp = Person()
    # emp.name = 'binbinbin'
    # emp.save()

    # return render(request, 'basic/404.html')
    if (request.method == 'POST'):
        formData = request.POST
        print(formData)
    else:
        print('hi() else')
    return HttpResponse('提交表单成功')

    # def index(request):
    #     return render(request, '404.html')




