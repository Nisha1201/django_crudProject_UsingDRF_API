from django.shortcuts import render,HttpResponseRedirect
from  .forms import StudentRegistration
from .models import User
# Create your views here.

#For Add new item and Show all items: 
def add_show(request):
    if request.method == 'POST':
        fm=StudentRegistration(request.POST)
        # print(fm)
        # print(request.POST)
        if fm.is_valid():
        #    nm= fm.cleaned_data['name']
        #    print(nm)
        #    em= fm.cleaned_data['email']
        #    print(em)
        #    pw= fm.cleaned_data['password']
        #    reg=User(name=nm ,email=em, password=pw)
        #    print(reg)
        
        #    reg.save()
        #    print(reg)
            fm.save()
        #    print(fm)
            fm=StudentRegistration()
        #    print(fm)
            return HttpResponseRedirect('/')
        
    else:
        fm=StudentRegistration()
        # print(fm)
    stud=User.objects.all()
    # print(stud.list)
    return render(request,'add_show.html',{'form':fm,'stu':stud})

#for update/edit:
def update_data(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        # print(pi,"yes post")
        fm=StudentRegistration(request.POST,instance=pi)
        # print(fm ,"yes post")
        # print(request.POST)
        if fm.is_valid():
            print(fm.is_valid())
            fm.save()
        print(fm,"yes post")
        return HttpResponseRedirect('/')
    else:
          pi=User.objects.get(pk=id)
          print(pi)
          fm=StudentRegistration(instance=pi)
          print(fm) 
    return render(request,'update.html',{'form':fm})
    

#For delete item:
def delete_data(request,id):
    if request.method =='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


