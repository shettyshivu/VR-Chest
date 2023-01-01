from django.shortcuts import render, redirect
from .models import Feedback, Appointment, Gallery_Image, Review, Article
# import googlemaps
# import pandas as pd
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .forms import ReviewForm, ArticleForm
from datetime import date, datetime
from slugify import slugify

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
        obj= Appointment(Name=name,Mobileno=contact, Email=email, Date=date, Time=time, Doctor=doctor)
        obj.save()
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
    return redirect('/')
    
@login_required(login_url='/login')
@csrf_exempt
def staff(request):
    a = Appointment.objects.all()
    an=0
    x= len(a)
    for i in a:
        if i.RequestStatus==2 :
            if i.Date < date.today():
                an=an+1
            if i.Date ==date.today() and i.Time <= datetime.now().time():
                an=an+1
    r= Review.objects.all()
    rn = len(r)
    f= Feedback.objects.all()
    fn=len(f)
    return render(request, 'staff.html',{'a':an, 'r':rn, 'f':fn})

@login_required(login_url = '/login')
def showAppointments (request):
    appointments = Appointment.objects.all() 
    return render(request, 'showAppointments.html', {'appointments':appointments})

@login_required(login_url='/login')
@csrf_exempt
def handleRequests(request):
        appointments = Appointment.objects.all()
        pending=[]
        for appointment in appointments :
            if appointment.RequestStatus == 1 :
                pending.append(appointment)
        return render(request, 'handleRequests.html',{'appointments':pending})

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
    appointments = Appointment.objects.all()
    accepted=[]
    for appointment in appointments :
        if appointment.RequestStatus == 2 :
            accepted.append(appointment)
    return render(request, 'acceptedRequests.html',{'appointments':accepted})


@login_required(login_url='/login')
@csrf_exempt
def showRejectRequests(request):
    appointments = Appointment.objects.all()
    rejected=[]
    for appointment in appointments :
        if appointment.RequestStatus == 3 :
            rejected.append(appointment)
    return render(request, 'rejectedRequests.html',{'appointments':rejected})


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
    appointments = Appointment.objects.all() 
    x=[]
    for a in appointments:
        if a.RequestStatus==2:
            if a.Date > date.today():
                x.append(a)
            if a.Date== date.today() and a.Time >= datetime.now().time():
                x.append(a)              
    return render(request, 'showAppointments.html', {'appointments':x})


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
        slug = slugify(title)
        obj= Article(title=title, content=content,slug=slug)
        obj.save()
        return redirect('/staff')


def articles(request):
    obj=Article.objects.all()
    return render(request,'articles.html', {'articles':obj})


def individualArticle(request, article_slug):
    obj=Article.objects.get(slug=article_slug)
    l = [obj]
    return render(request, 'individualArticle.html', {'articles':l})
        