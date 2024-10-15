import datetime
import smtplib
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import *
import random
# Create your views here.

syspath=r"C:\Users\Mohammed Nafih\OneDrive\Desktop\hawks eye project\Thief_Detection\Thief\static\\"
# syspath=r"D:\2023-2024\LBS_THIEFDETECTION\Thief_Detection\Thief\static\\"

def log(request):
    return render(request,"index.html")

def log_post(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    data = login.objects.filter(username=username,password=password)
    if data.exists():
        data = data[0]
        request.session['lid'] = data.id
        request.session['lg'] = "lin"

        if data.type =='admin':
            return redirect('/admin_home')
        if data.type =='user':
            return redirect('/user_home')
        if data.type == 'policestation':
            return redirect('/police_home')
    else:
        return HttpResponse("<script>alert('Invalid User');window.location='/'</script>")


def admin_home(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")

    return render(request,"admin/index.html")

def police_home(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")

    return render(request,"policestation/index.html")


def user_home(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")

    return render(request,"User/index.html")

# Police station management

def police_add(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        return render(request,"admin/add_police.html")

def police_add_post(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        name = request.POST['textfield']
        place = request.POST['textfield2']
        post = request.POST['textfield3']
        pin = request.POST['textfield4']
        email = request.POST['textfield5']
        contact = request.POST['textfield6']

        res = random.randint(0000,9999)


        lob = login.objects.filter(username=email)
        if lob.exists():
            return HttpResponse("<script>alert('Already Exist');window.location='/view_police#kk'</script>")
        else:
            log_obj = login()
            log_obj.username = email
            log_obj.password = res
            log_obj.type = 'policestation'
            log_obj.save()

            obj = police_station()
            obj.name = name
            obj.place = place
            obj.post = post
            obj.pin = pin
            obj.email = email
            obj.contact = contact
            obj.LOGIN = log_obj
            obj.save()

            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)

                gmail.ehlo()

                gmail.starttls()

                gmail.login('vvrr2731@gmail.com', 'ajay1490')

            except Exception as e:
                print("Couldn't setup email!!" + str(e))

            msg = MIMEText("Your  Password for SecureX is  " + str(res))

            msg['Subject'] = 'Verification'

            msg['To'] = email

            msg['From'] = 'vvrr2731@gmail.com'

            try:

                gmail.send_message(msg)

            except Exception as e:

                print("COULDN'T SEND EMAIL", str(e))
            return HttpResponse("<script>alert('Success');window.location='/view_police#kk'</script>")

def view_police(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        data = police_station.objects.all()
        return render(request,"admin/view_police.html",{"data":data})

def update_police(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        data = police_station.objects.get(id=id)
        return render(request,"admin/update_police.html",{"data":data})

def update_police_post(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        name = request.POST['textfield']
        place = request.POST['textfield2']
        post = request.POST['textfield3']
        pin = request.POST['textfield4']
        email = request.POST['textfield5']
        contact = request.POST['textfield6']
        police_station.objects.filter(id=id).update(name = name,place=place,post=post,pin=pin,email=email,contact=contact)
        return HttpResponse("<script>alert('Updated');window.location='/view_police#kk'</script>")

def delete_police(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        police_station.objects.get(id=id).delete()

        return HttpResponse("<script>alert('Deleted');window.location='/view_police#kk'</script>")

# Crminal category Management

def add_criminal_category(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        return render(request,"admin/add_category.html")

def add_criminal_category_post(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        category = request.POST['textfield']
        if crime_category.objects.filter(category_name=category).exists():
            return HttpResponse("<script>alert('The crime category "+category+" is already exists');window.location='/view_category#kk'</script>")
        obj = crime_category()
        obj.category_name = category
        obj.save()
        return HttpResponse("<script>alert('Success');window.location='/view_category#kk'</script>")

def view_category(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        data = crime_category.objects.all()
        return render(request,"admin/view_category.html",{"data":data})

def delete_category(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        crime_category.objects.get(id=id).delete()
        return HttpResponse("<script>alert('Deleted');window.location='/view_category#kk'</script>")

def view_detection_details(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        data = alert.objects.all()
        return render(request,"admin/view_detection_details.html",{"data":data})

def view_criminals(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        data = criminals.objects.all()
        return render(request,"admin/view_criminals.html",{"data":data})

def view_user(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        data = user.objects.all()
        return render(request,"admin/view_user.html",{"data":data})

def logout(request):
    request.session['lg']=" "
    return redirect('/')

def view_complaint(request):
    if request.session['lg'] != "lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    cobj = complaint.objects.all()
    return render(request,"admin/view_complaint.html",{"data":cobj,"dat":datetime.datetime.now().strftime("%Y-%m-%d")})




def view_complaint_post(request):
    if request.session['lg'] != "lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    btn = request.POST['sam']
    if btn == 'SEARCH':
        n=request.POST['dt']
        cobj = complaint.objects.filter(Q(cdate=n)|Q(rdate=n))
        return render(request,"admin/view_complaint.html",{"data":cobj,"dat":datetime.datetime.now().strftime("%Y-%m-%d")})
    else:
        t= request.POST['t']
        cid=request.POST['cid']
        complaint.objects.filter(id=cid).update(reply=t,rdate=datetime.datetime.now().strftime("%Y-%m-%d"))
        return HttpResponse("<script>alert('Reply updated successfully');window.location='/view_complaint#kk'</script>")

def view_complaint_post1(request):
    if request.session['lg'] != "lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    btn = request.POST['sam']
    if btn == 'SEARCH':
        n = request.POST['dt']
        cobj = complaint.objects.filter(Q(cdate=n) | Q(rdate=n))
        return render(request, "admin/view_complaint.html",
                      {"data": cobj, "dat": datetime.datetime.now().strftime("%Y-%m-%d")})
    else:
        t = request.POST['t']
        cid = request.POST['cid']
        complaint.objects.filter(id=cid).update(reply=t, rdate=datetime.datetime.now().strftime("%Y-%m-%d"))
        return HttpResponse(
            "<script>alert('Reply updated successfully');window.location='/view_complaint#kk'</script>")


###########################################################################################

# police station module

def view_profile(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        data = police_station.objects.get(LOGIN=request.session['lid'])
        # print(data)
        return render(request,"policestation/view_profile.html",{"data":data})

# criminal Management

def add_criminal(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        data = crime_category.objects.all()
        return render(request,"policestation/add_criminal.html",{"data":data})

def add_criminal_post(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        name = request.POST['textfield']
        gender = request.POST['RadioGroup1']
        age = request.POST['textfield2']
        place = request.POST['textfield3']
        post = request.POST['textfield4']
        pin = request.POST['textfield5']
        contact = request.POST['textfield6']
        photo = request.FILES['fileField2']

        fs = FileSystemStorage()
        dt = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        fs.save(syspath+"photo\\"+ dt + '.jpg', photo)
        photo = '/static/photo/' + dt + '.jpg'

        obj = criminals()
        obj.POLICE = police_station.objects.get(LOGIN=request.session['lid'])
        obj.name = name
        obj.gender = gender
        obj.age = age
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.contact = contact
        obj.photo = photo
        obj.save()
        return HttpResponse("<script>alert('Success');window.location='/view_criminal#kk'</script>")

def view_criminal(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        data = criminals.objects.all()
        return render(request,"policestation/view_criminal.html",{"data":data})

def update_criminal(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        data = criminals.objects.get(id=id)
        data1 = crime_category.objects.all()
        return render(request,"policestation/update_criminal.html",{"data":data,"data1":data1})

def update_criminal_post(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        name = request.POST['textfield']
        gender = request.POST['RadioGroup1']
        age = request.POST['textfield2']
        place = request.POST['textfield3']
        post = request.POST['textfield4']
        pin = request.POST['textfield5']
        contact = request.POST['textfield6']
        try:
            photo = request.FILES['fileField2']
            fs = FileSystemStorage()
            dt = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            fs.save(syspath + "photo\\" + dt + '.jpg', photo)
            photo = '/static/photo/' + dt + '.jpg'
            criminals.objects.filter(id=id).update(name=name,gender=gender,age=age,place=place,post=post,pin=pin,contact=contact,photo=photo)
        except Exception as e:
            criminals.objects.filter(id=id).update(name=name,gender=gender,age=age,place=place,post=post,pin=pin,contact=contact)
        return HttpResponse("<script>alert('Updated');window.location='/view_criminal#kk'</script>")

def delete_criminal(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        criminals.objects.get(id=id).delete()
        return HttpResponse("<script>alert('Deleted');window.location='/view_criminal#kk'</script>")


def view_users(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:

        data = user.objects.all()
        return render(request,"policestation/view_user.html",{"data":data})

def view_crminal_alert(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:

        data = alert.objects.filter(CRIMINALS__POLICE__LOGIN=request.session['lid'])
        return render(request, "policestation/view_criminal_alert.html",{"data":data})

def add_crimehistory(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    request.session['hid']=id
    data = crime_category.objects.all()
    data2 = crimehistory.objects.filter(CRIMINAL__id=id)
    return render(request,"policestation/add_crimehistory.html",{"id":id,"data":data2,"d":data,"rdate":datetime.datetime.now().strftime("%Y-%m-%d")})


def add_crimehistory_post(request, id):
    c=request.POST['select']
    d=request.POST['textfield']
    h=request.POST['textfield2']
    hobj = crimehistory()
    hobj.date=d
    hobj.CATEGORY_id=c
    hobj.CRIMINAL_id=id
    hobj.history=h
    hobj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/add_crimehistory/" + str(
        request.session['hid']) + "#kk'</script>")


def delete_history(request,id):
    crimehistory.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Delete successfully');window.location='/add_crimehistory/"+str(request.session['hid'])+"#kk'</script>")

######################################################################################################



def user_registration(request):
    return render(request,"reg.html")

def regpost(request):
    name = request.POST['Username']
    place = request.POST['pl']
    post = request.POST['po']
    pin = request.POST['pi']
    email = request.POST['email']
    contact = request.POST['ph']
    password = request.POST['p']
    photo = request.FILES['pic']
    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fs.save(syspath+"photo\\" + d + '.jpg', photo)
    photo = '/static/photo/' + d + '.jpg'
    data = login.objects.filter(username=email)
    if data.exists():
        return HttpResponse("<script>alert('Email already exists');window.location='/'</script>")

    log_obj = login()
    log_obj.username = email
    log_obj.password = password
    log_obj.type = 'user'
    log_obj.save()
    obj = user()
    obj.name = name
    obj.place = place
    obj.post = post
    obj.pin = pin
    obj.email = email
    obj.contact = contact
    obj.photo = photo
    obj.LOGIN = log_obj
    obj.save()
    return HttpResponse("<script>alert('Registered successfully');window.location='/'</script>")


def email_already_exist(request):
    em = request.POST['type']
    data = login.objects.filter(username=em)
    if data.exists():
        return JsonResponse({"status":"none"})
    else:
        return JsonResponse({"status":"ok"})


def user_view_profile(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    vid = request.session['lid']
    res = user.objects.get(LOGIN=vid)
    return render(request,"User/viewprofile.html",{"i":res})


def user_view_police(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        data = police_station.objects.all()
        return render(request,"User/view_police.html",{"data":data})


def user_view_criminals(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    else:
        data = criminals.objects.all()
        return render(request,"User/view_criminals.html",{"data":data})


def user_view_crimehistory(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    data = crime_category.objects.all()
    data2 = crimehistory.objects.filter(CRIMINAL__id=id)
    return render(request,"User/view_crimehistory.html",{"id":id,"data":data2,"d":data,"rdate":datetime.datetime.now().strftime("%Y-%m-%d")})


def add_camera(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    res = camera.objects.filter(USER__LOGIN=request.session['lid'])
    return render(request,"User/add_camera.html",{"data":res})


def add_camera_post(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    camera_no = request.POST['camera_no']
    if camera.objects.filter(camera_number=camera_no,USER__LOGIN=request.session['lid']).exists():
        return HttpResponse("<script>alert('Details already exists');window.location='/add_camera#kk'</script>")

    obj = camera()
    obj.camera_number = camera_no
    obj.USER=user.objects.get(LOGIN_id=request.session['lid'])
    obj.save()
    return HttpResponse("<script>alert('Details added successfully');window.location='/add_camera#kk'</script>")
def user_view_camera(request):
    data=camera.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request, "User/view_camera.html", {'data':data})

def delete_camera(request,cid):
    camera.objects.filter(id=cid).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/add_camera#kk'</script>")


#### Femiliar person Management

def user_add_familiar_person(request):
    if request.session['lg'] != "lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    return render(request,"User/add_person.html")

def user_add_familiar_person_post(request):
    lid = request.session['lid']
    name = request.POST['name']
    place = request.POST['place']
    contact = request.POST['contact']
    photo = request.FILES['pic']
    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fs.save(syspath+"photo\\" + d + '.jpg', photo)
    photo = '/static/photo/' + d + '.jpg'
    obj = familiar_person()
    obj.F_name = name
    obj.F_place = place
    obj.F_contact = contact
    obj.F_image = photo
    obj.USER = user.objects.get(LOGIN=lid)
    obj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/user_view_familiar_person#kk'</script>")


def user_view_familiar_person(request):
    if request.session['lg'] != "lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")

    lid = request.session['lid']
    res = familiar_person.objects.filter(USER__LOGIN=lid)
    return render(request,"User/view_person.html",{"data":res})

def user_delete_familiar_person(request,fid):
    familiar_person.objects.get(id=fid).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/user_view_familiar_person#kk'</script>")


def user_update_familiar_persons(request,fid):
    if request.session['lg'] != "lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")


    res = familiar_person.objects.get(id=fid)
    return render(request,"User/update_person.html",{"data":res})


def user_update_familiar_person_post(request,fid):
    try:

        name = request.POST['name']
        place = request.POST['place']
        contact = request.POST['contact']
        photo = request.FILES['pic']
        fs = FileSystemStorage()
        d = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs.save(syspath+"photo\\" + d + ".jpg", photo)
        path = '/static/photo/' + d + ".jpg"
        familiar_person.objects.filter(id=fid).update(F_name=name,F_place =place,F_contact=contact,F_image=path)
        return HttpResponse(
            "<script>alert('Updated successfully');window.location='/user_view_familiar_person#kk'</script>")


    except Exception as e:


        name = request.POST['name']
        place = request.POST['place']
        contact = request.POST['contact']
        familiar_person.objects.filter(id=fid).update(F_name=name, F_place=place,F_contact=contact)
        return HttpResponse(
            "<script>alert('Updated successfully');window.location='/user_view_familiar_person#kk'</script>")


def user_view_comp(request):
    if request.session['lg'] != "lin":
        return HttpResponse("<script>alert('Please Login again');window.location='/'</script>")
    lid = request.session['lid']
    cobj = complaint.objects.filter(USER__LOGIN=lid)
    return render(request,"User/view_complaint.html",{"data":cobj,"dat":datetime.datetime.now().strftime("%Y-%m-%d")})


def add_complaint(request):
    return render(request,"User/send_complaint.html")


def add_complaint_post(request):
    c= request.POST['textfield']
    cobj = complaint()
    cobj.complaint = c
    cobj.USER = user.objects.get(LOGIN=request.session['lid'])
    cobj.save()
    return HttpResponse("<script>alert('Registered successfully');window.location='/user_view_comp#kk'</script>")

def user_view_alert(request,t):
    lid = request.session['lid']
    if t == 'p':
        res = familiar_log.objects.filter(FAMILIAR_PERSON__USER__LOGIN=lid)
        return render(request,"User/view_detection_details.html",{"data":res,"t":t})
    if t == "v":
        res = visitor_log.objects.filter(CAMERA__USER__LOGIN=login.objects.get(id=lid))
        return render(request, "User/view_detection_details.html", {"data": res, "t": t})
    if t == "c":
        res = alert.objects.filter(CAMERA__USER__LOGIN=login.objects.get(id=lid))
        return render(request, "User/view_detection_details.html", {"data": res, "t": t})