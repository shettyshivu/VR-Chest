from django.shortcuts import render, redirect
from .models import Feedback, Appointment, Gallery_Image, Review, Article
# import googlemaps
# import pandas as pd
import calendar
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .forms import ReviewForm, ArticleForm
from datetime import date, datetime
from slugify import slugify
from django.core.mail import send_mail

# Create your views here.
def home(request):
    images = Gallery_Image.objects.all()
    reviews = Review.objects.all()  
    return render(request,'home.html', {'images':images, 'reviews':reviews})

def saveFeedback(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        msg=request.POST.get('msg')
        obj = Feedback (Name = name, Email=email, Messege=msg)
        obj.save()  
        subject = 'VR Chest and Women Care'
        msg='Thank you for your valueable feedback!\n\n Regards, \n VR Chest and Women Care'
        send_mail(subject, msg , 'karthzz003@gmail.com', [email], fail_silently=True)
        messages.info(request,'Thanks for your valuable feedback!')
        return redirect('/')

def appointment(request):
    return render(request, 'appointment.html')

def appointmentConfirm(request):
    if request.method=='POST':
        name=request.POST.get('name')
        contact=request.POST.get('mobileno')
        email=request.POST.get('email')
        date=request.POST.get('date')
        time=request.POST.get('time')
        doctor=request.POST.get('doctor')
        born = datetime.weekday()
        day = calendar.day_name[born]
        if( doctor == "Dr. Vasunethra Kasargod" and (day =='Tuesday' or day == 'Sunday' or time<17 or time>21)):
            return render(request, 'detailswrong.html') 
        obj= Appointment(Name=name,Mobileno=contact, Email=email, Date=date, Time=time, Doctor=doctor)
        obj.save()
        subject = 'VR Chest and Women Care'
        msg='Appointment request has been sent!\n\nThank you for using our website to book your appointment. You will receive a confirmation mail once your request is accpeted. \n\nRegards, \nVR Chest and Women Care'
        try:
            send_mail(subject, msg , 'karthzz003@gmail.com', [email], fail_silently=False)
        except:
            return render(request, 'mailfail.html')
        messages.info(request,'Appointment Request Sent!')
        return redirect('/')

@csrf_exempt
def logins(request):
    if request.method=='POST' :
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('staff')
        else :
            messages.info(request,'Invalid Credentials!')
            return redirect('login')
    else :
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    messages.info(request,'Succesfully logged out!')
    return redirect('/')


@login_required(login_url='/login')
@csrf_exempt
def staff(request):
    return render(request, 'staff.html')


@login_required(login_url = '/login')
def showAppointments (request):
    all_appointments = Appointment.objects.all() 
    vasu_appointments = Appointment.objects.filter(Doctor = "Dr. Vasunetra Kasargod")
    veni_appointments = Appointment.objects.filter(Doctor="Dr. Veni N")
    app_all_new = sorted(all_appointments, key=lambda x: (x.Date, x.Time), reverse=True)
    app_all_old = sorted(all_appointments, key=lambda x: (x.Date, x.Time))
    vasu_new = sorted(vasu_appointments, key=lambda x: (x.Date, x.Time), reverse=True)
    vasu_old = sorted(vasu_appointments, key=lambda x: (x.Date, x.Time))
    veni_new= sorted(veni_appointments, key=lambda x: (x.Date, x.Time), reverse=True)
    veni_old = sorted(veni_appointments, key=lambda x: (x.Date, x.Time))
    return render(request, 'showAppointments.html', {'app_all_new':app_all_new,'app_all_old':app_all_old,'vasu_new':vasu_new,'vasu_old':vasu_old,'veni_new':veni_new,'veni_old':veni_old})


@login_required(login_url='/login')
@csrf_exempt
def handleRequests(request):
        all_appointments = Appointment.objects.filter(RequestStatus=1) 
        vasu_appointments = Appointment.objects.filter(Doctor = "Dr. Vasunetra Kasargod", RequestStatus =1)
        veni_appointments = Appointment.objects.filter(Doctor="Dr. Veni N", RequestStatus=1)
        app_all_new = sorted(all_appointments, key=lambda x: (x.Date, x.Time), reverse=True)
        app_all_old = sorted(all_appointments, key=lambda x: (x.Date, x.Time))
        vasu_new = sorted(vasu_appointments, key=lambda x: (x.Date, x.Time), reverse=True)
        vasu_old = sorted(vasu_appointments, key=lambda x: (x.Date, x.Time))
        veni_new= sorted(veni_appointments, key=lambda x: (x.Date, x.Time), reverse=True)
        veni_old = sorted(veni_appointments, key=lambda x: (x.Date, x.Time))
        return render(request, 'handleRequests.html', {'app_all_new':app_all_new,'app_all_old':app_all_old,'vasu_new':vasu_new,'vasu_old':vasu_old,'veni_new':veni_new,'veni_old':veni_old})

@login_required(login_url='/login')
@csrf_exempt
def requestAccept(request):
    try:
        request_id = request.GET.get('s_id')
        appoint = Appointment.objects.get(id=request_id)
        appoint.RequestStatus=2
        appoint.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        print(e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/login')
@csrf_exempt
def requestReject(request):
    try:
        request_id = request.GET.get('s_id')
        appoint = Appointment.objects.get(id=request_id)
        appoint.RequestStatus=3
        appoint.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        print(e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/login')
@csrf_exempt
def showAcceptRequests(request):
    all_appointments = Appointment.objects.filter(RequestStatus=2) 
    vasu_appointments = Appointment.objects.filter(Doctor = "Dr. Vasunetra Kasargod", RequestStatus =2)
    veni_appointments = Appointment.objects.filter(Doctor="Dr. Veni N", RequestStatus=2)
    app_all_new = sorted(all_appointments, key=lambda x: (x.Date, x.Time), reverse=True)
    app_all_old = sorted(all_appointments, key=lambda x: (x.Date, x.Time))
    vasu_new = sorted(vasu_appointments, key=lambda x: (x.Date, x.Time), reverse=True)
    vasu_old = sorted(vasu_appointments, key=lambda x: (x.Date, x.Time))
    veni_new= sorted(veni_appointments, key=lambda x: (x.Date, x.Time), reverse=True)
    veni_old = sorted(veni_appointments, key=lambda x: (x.Date, x.Time))
    return render(request, 'acceptedRequests.html', {'app_all_new':app_all_new,'app_all_old':app_all_old,'vasu_new':vasu_new,'vasu_old':vasu_old,'veni_new':veni_new,'veni_old':veni_old})


@login_required(login_url='/login')
@csrf_exempt
def showRejectRequests(request):
    all_appointments = Appointment.objects.filter(RequestStatus=3) 
    vasu_appointments = Appointment.objects.filter(Doctor = "Dr. Vasunetra Kasargod", RequestStatus =3)
    veni_appointments = Appointment.objects.filter(Doctor="Dr. Veni N", RequestStatus=3)
    app_all_new = sorted(all_appointments, key=lambda x: (x.Date, x.Time), reverse=True)
    app_all_old = sorted(all_appointments, key=lambda x: (x.Date, x.Time))
    vasu_new = sorted(vasu_appointments, key=lambda x: (x.Date, x.Time), reverse=True)
    vasu_old = sorted(vasu_appointments, key=lambda x: (x.Date, x.Time))
    veni_new= sorted(veni_appointments, key=lambda x: (x.Date, x.Time), reverse=True)
    veni_old = sorted(veni_appointments, key=lambda x: (x.Date, x.Time))
    return render(request, 'rejectedRequests.html', {'app_all_new':app_all_new,'app_all_old':app_all_old,'vasu_new':vasu_new,'vasu_old':vasu_old,'veni_new':veni_new,'veni_old':veni_old})


@login_required(login_url='/login')
@csrf_exempt
def showTodayAppointments(request):
    all_appointments = Appointment.objects.filter(RequestStatus=2, Date=date.today()) 
    vasu_appointments = Appointment.objects.filter(Doctor = "Dr. Vasunetra Kasargod", RequestStatus =2 , Date=date.today())
    veni_appointments = Appointment.objects.filter(Doctor="Dr. Veni N", RequestStatus=2 , Date=date.today())
    app_all_new = sorted(all_appointments, key=lambda x: (x.Date, x.Time), reverse=True)
    app_all_old = sorted(all_appointments, key=lambda x: (x.Date, x.Time))
    vasu_new = sorted(vasu_appointments, key=lambda x: (x.Date, x.Time), reverse=True)
    vasu_old = sorted(vasu_appointments, key=lambda x: (x.Date, x.Time))
    veni_new= sorted(veni_appointments, key=lambda x: (x.Date, x.Time), reverse=True)
    veni_old = sorted(veni_appointments, key=lambda x: (x.Date, x.Time))
    return render(request, 'todayAppointments.html', {'app_all_new':app_all_new,'app_all_old':app_all_old,'vasu_new':vasu_new,'vasu_old':vasu_old,'veni_new':veni_new,'veni_old':veni_old})


@login_required(login_url='/login')
@csrf_exempt
def showGalleryImages(request):
    images = Gallery_Image.objects.all()
    return render(request,'showGallery.html',{'images':images})


@login_required(login_url='/login')
@csrf_exempt
def deleteGalleryImages(request):
    try:
        delete_id = request.GET.get('s_id')
        delete_image = Gallery_Image.objects.get(id=delete_id)
        delete_image.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        print(e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/login')
@csrf_exempt
def addGalleryImages(request):
    if request.method=="POST":   
        img= request.FILES['uploadedImage']
        obj=Gallery_Image(Image=img)
        obj.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/login')
@csrf_exempt
def addReviews(request):
    return render(request, 'addReview.html')


@login_required(login_url='/login')
@csrf_exempt
def submitReview(request):
    if request.method=='POST':
        name= request.POST.get("name")
        review= request.POST.get("review")
        rating= request.POST.get("rating")
        obj= Review(Review_text=review, Review_username=name, rating=rating)
        obj.save()
        return redirect('/staff')


@login_required(login_url='/login')
@csrf_exempt
def editOrDeleteReviews(request):
    reviews = Review.objects.all()
    return render(request,'showReview.html',{'reviews':reviews})


@login_required(login_url='/login')
@csrf_exempt
def deleteReview(request):
    try:
        delete_id = request.GET.get('s_id')
        delete_review = Review.objects.get(id=delete_id)
        delete_review.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        print(e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/login')
@csrf_exempt
def showFeedback(request):
    feedbacks=Feedback.objects.all()
    return render(request,'showFeedback.html' ,{'feedbacks':feedbacks})


@login_required(login_url='/login')
@csrf_exempt
def deleteFeedback(request):
    try:
        delete_id = request.GET.get('s_id')
        delete_feedback = Feedback.objects.get(id=delete_id)
        delete_feedback.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        print(e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/login')
@csrf_exempt
def editReview(request, review_id):
    review= Review.objects.get(id=review_id)
    form = ReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect("edit-or-delete-reviews")
    return render(request, 'editReviews.html',{'review':review, 'form':form})


@login_required(login_url='/login')
@csrf_exempt
def showUpcomingAppointments(request):
    all_appointments = Appointment.objects.filter(RequestStatus=2) 
    vasu_appointments = Appointment.objects.filter(Doctor = "Dr. Vasunetra Kasargod", RequestStatus =2)
    veni_appointments = Appointment.objects.filter(Doctor="Dr. Veni N", RequestStatus=2)
    app_all_new1 = sorted(all_appointments, key=lambda x: (x.Date, x.Time), reverse=True)
    app_all_old1 = sorted(all_appointments, key=lambda x: (x.Date, x.Time), )
    vasu_new1 = sorted(vasu_appointments, key=lambda x: (x.Date, x.Time), reverse=True)
    vasu_old1 = sorted(vasu_appointments, key=lambda x: (x.Date, x.Time))
    veni_new1= sorted(veni_appointments, key=lambda x: (x.Date, x.Time), reverse=True)
    veni_old1 = sorted(veni_appointments, key=lambda x: (x.Date, x.Time))
    app_all_new=[]
    app_all_old=[]
    vasu_new=[]
    vasu_old=[]
    veni_new=[]
    veni_old=[]
    for a in app_all_new1:
        if a.Date > date.today():
            app_all_new.append(a)
        if (a.Date== date.today() and a.Time >= datetime.now().time()):
            app_all_new.append(a)   
    for a in app_all_old1:
        if a.Date > date.today():
            app_all_old.append(a)
        if a.Date== date.today() and a.Time >= datetime.now().time():
            app_all_old.append(a) 
    for a in veni_new1:
        if a.Date > date.today():
            veni_new.append(a)
        if a.Date== date.today() and a.Time >= datetime.now().time():
            veni_new.append(a)   
    for a in veni_old1:
        if a.Date > date.today():
            veni_old.append(a)
        if a.Date== date.today() and a.Time >= datetime.now().time():
            veni_old.append(a)   
    for a in vasu_new1:
        if a.Date > date.today():
            vasu_new.append(a)
        if a.Date== date.today() and a.Time >= datetime.now().time():
            vasu_new.append(a) 
    for a in vasu_old1:
        if a.Date > date.today():
            vasu_old.append(a)
        if a.Date== date.today() and a.Time >= datetime.now().time():
            vasu_old.append(a)   
    return render(request, 'showUpcomingAppointments.html', {'app_all_new':app_all_new,'app_all_old':app_all_old,'vasu_new':vasu_new,'vasu_old':vasu_old,'veni_new':veni_new,'veni_old':veni_old})           
    

def facilities(request):
    return render(request, 'facilities.html')

def gallery(request):
    images = Gallery_Image.objects.all()
    return render(request,'gallery.html',{'images':images})


@login_required(login_url='/login')
@csrf_exempt
def addArticle(request):
    return render(request, 'addArticle.html')


@login_required(login_url='/login')
@csrf_exempt
def editOrDeleteArticle(request):
    articles= Article.objects.all()
    return render(request, 'showArticles.html',{'articles':articles})


@login_required(login_url='/login')
@csrf_exempt
def deleteArticle(request):
    try:
        delete_id = request.GET.get('a_id')
        delete_article = Article.objects.get(id=delete_id)
        delete_article.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        print(e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/login')
@csrf_exempt
def editArticle(request, article_id):
    article= Article.objects.get(id=article_id)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect("edit-or-delete-article")
    return render(request, 'editArticles.html',{'article':article, 'form':form})


@login_required(login_url='/login')
@csrf_exempt
def submitArticle(request):
    if request.method=='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        link = request.POST.get('link')
        slug = slugify(title)
        obj= Article(title=title, content=content,slug=slug, link=link)
        obj.save()
        return redirect('/staff')


def articles(request):
    obj=Article.objects.all()
    return render(request,'articles.html', {'articles':obj})


def individualArticle(request, article_slug):
    obj=Article.objects.get(slug=article_slug)
    l = [obj]
    return render(request, 'individualArticle.html', {'articles':l})

def vasuAppointments(request):
    return render(request,'vasuAppointments.html')

def veniAppointments(request):
    return render(request, 'veniAppointments.html')
        