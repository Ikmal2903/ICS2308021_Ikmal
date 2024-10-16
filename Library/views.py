from django.shortcuts import render, redirect
from Library.models import Student,Borrowing,Book,Course,Mentor
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

def index(request):
    context={
        'greeting':0,
    }
    return render(request,'index.html',context)

def view(request):
    context={
        'firstname':'Hanif Pablo',
    }
    return render(request,'view.html',context)


def database(request):
    student= Student.objects.all().values()
    book= Book.objects.all().values()
    borrowing= Borrowing.objects.all().values()

    context={
        'Student': student,
        'Book': book,
        'Borrowing': borrowing,
    }

    return render (request,"database.html",context)

def course(request):
    mycourse= Course.objects.all().values()
    context={
        'mycourse':mycourse,

    }
    if request.method=='POST':
        c_code= request.POST['code']
        c_desc= request.POST['description']
        data=Course(code=c_code, description=c_desc)
        data.save()
        dict={
            'message':'Data Save'
        }
    else:
        dict={
            'message':''
        }

    return render(request,'course.html',context)
def mentor(request):
    mymentor=Mentor.objects.all().values()
    context={
        'mymentor':mymentor,
    }
    if request.method=='POST':
        m_id=request.POST['menid']
        m_name=request.POST['menname']
        m_roomno=request.POST['menroomno']
        data=Mentor(m_id,m_name,m_roomno)
        data.save()
    return render(request,'newmentor.html',context)

def update_course(request,code):
    data=Course.objects.get(code=code)
    dict={
        'data':data
    }
    return render(request ,"update_course.html", dict)
def save_update_course(request,code):
    c_desc=request.POST['description']
    data=Course.objects.get(code=code)
    data.description=c_desc
    data.save()
    return HttpResponseRedirect(reverse("course"))
def update_mentor(request,menid):
    data=Mentor.objects.get(menid=menid)
    dict={
        'data':data
    }
    return render(request ,"update_mentor.html", dict)
def save_update_mentor(request,menid):
    c_name=request.POST['menname']
    c_roomno=request.POST['menroomno']
    data=Mentor.objects.get(menid=menid)
    data.menname=c_name
    data.menroomno=c_roomno
    data.save()
    return HttpResponseRedirect(reverse("mentor"))
def delete_course(request,code):
    data=Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse("course"))
def delete_mentor(request,menid):
    data=Mentor.objects.get(menid=menid)
    data.delete()
    return HttpResponseRedirect(reverse('mentor'))
def search_course(request):
    if request.method == 'GET':
        c_code= request.GET.get('c_code')

        if c_code:
            data=Course.objects.filter(code=c_code.upper())
        else:
            data= None
        context={
            'data':data,
        }
        return render(request,"search_course.html",context)
    return render(request,"search_course.html")
def search_mentor(request):
    if request.method == 'GET':
        m_id= request.GET.get('m_id')

        if m_id:
            data=Mentor.objects.filter(menid=m_id.upper())
        else:
            data= None
        context={
            'data':data,
        }
        return render(request,"search_mentor.html",context)
    return render(request,"search_mentor.html")


