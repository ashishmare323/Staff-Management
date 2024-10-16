from django.shortcuts import render, redirect
from .models import staff

from django.http import HttpResponse


# Create your views here.
# def dashboard(request):
#   return HttpResponse("HELLOOO!!!!!!!!!!!!!!!!!!!11")
def dashboard(request):
    obj = staff.objects.all()
    return render(request, "admin.html", {"obj": obj})


def add_staff(request):
    if request.method =='POST':
        s_name = request.POST['name']
     #   s_surname = request.POST['surname']
        s_age = request.POST['age']
        s_email = request.POST['email']
        s_contact = request.POST['contact']
        s_address = request.POST['address']
        s_profile = request.POST['profile']
        s_subject = request.POST['subject']
        obj = staff.objects.create(
            s_name=s_name,
         #   s_surname=s_surname,
            s_age=s_age,
            s_email=s_email,
            s_address=s_address,
            s_contact=s_contact,
            s_subject=s_subject,
            s_profile=s_profile,

        )
        obj.save()
        return redirect('/')
    return render(request, 'admin.html')

#def edit_staff(request,s_id):
 #   obj = staff.objects.get(s_id=s_id)
  #  return render(request,'admin.html')


def edit_staff(request,s_id):
  #  print("**********")
 #   print(s_id)
    if request.method == 'POST':
        i=staff.objects.get(s_id=s_id)
        i.s_name = request.POST.get('s_name')
        i.s_email = request.POST.get('s_email')
        i.s_contact = request.POST.get('s_contact')
        i.s_address = request.POST.get('s_address')
        i.save()
        return redirect('/')
    return render(request,'admin.html')


def delete_staff(request,s_id):
    staff.objects.get(s_id=s_id).delete()
    return redirect('/')