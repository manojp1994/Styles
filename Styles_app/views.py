from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import loader
from forms import DetailsForm,ExpertForm,Reviews_ratingForm
from django.views.decorators.csrf import csrf_exempt
from Styles_app.models import *
import random
from .models import Otp
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from .models import Salon

# Create your views here.
def first(request):
    args={}
    return render_to_response('first.html',args)

def index1(request):
    args={}
    return render_to_response('index1.html',args)

# This is for login page
def login(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('SignIn.html',args)

# This is for validating the login page.
def login_check(request):
	# username = request.POST.get('username','')
    email = request.POST.get('email','')
    password = request.POST.get('password','')
    try:
		user = Details.objects.get(email=email)
    except Details.DoesNotExist:
		return HttpResponseRedirect('/Styles')
    if user is not None and user.registered == True:
		if user.password == password:
			request.session['name'] = email
			return HttpResponseRedirect('/Styles/index1/')
		else:
			html = "<html><body>Password Error</body></html>"
			return HttpResponse(html)
    else:
		html = "<html><body>OTP Error</body></Html>"
		return HttpResponse(html)

# This is for registration page.
def registration(request):
    args = {}
    args.update(csrf(request))
    request.session['name'] = ''
    return render_to_response('Registration.html',args)

# This is for registration page.   
def otp(request):
    args = {}
    args.update(csrf(request))
    print "cococ"
    return render_to_response('otp.html',args)

# This is for otp checking.
def otpcheck(request):
    email = request.POST.get('email','')
    otp = request.POST.get('otp','')
    print email
    print otp
    try:
        user = Otp.objects.get(mail=email)
        x=Details.objects.get(email=user.mail)
        print user
        print user.otp
    except Otp.DoesNotExist:
        return HttpResponseRedirect('/Styles')
    if user is not None:
        if otp == user.otp:
            request.session['name'] = otp
            x.registered=True
            x.save()
            return render_to_response('index1.html')
            # return HttpResponseRedirect('/pikachu/index1/')
        else:
            html = "<html><body>otp Error</body></html>"
            return HttpResponse(html)
    else:
        html = "<html><body>email Error</body></Html>"
        return HttpResponse(html)
# This is for Registration checking page
def registration_check(request):
    form = DetailsForm()
    if request.POST:
        form = DetailsForm(request.POST)
        name = request.POST.get('mobilenum')
        print name
        if form.is_valid():
            form.registered = False
            print 'hi'
            email = form.cleaned_data['email']
            a=random.randint(11111,99999)
            print 'check 1'
            print email
            print 'check'
            print a
            p = Otp(otp = a, mail = email)
            p.save()
            frommail = email
            print frommail
            ans = str(a)
            msg = EmailMessage("Hi", "Thanks for registering to site. Please use this OTP to verify your E-mail.\n" + ans, to=[frommail])
            msg.send()
            form.save()
            return HttpResponseRedirect('/Styles/login/')
        else:           
            return render_to_response('first.html',{'form':form})
    return render_to_response('registration.html',{'form':form}, context_instance=RequestContext(request))

# Logout functionality
def logout(request):
    request.session['name'] = ''
    return HttpResponseRedirect('/Styles')

# About
def about(request):
    args={}
    return render_to_response('About.html',args)

# Contact
def contact(request):
    args={}
    return render_to_response('contact.html',args)

# search
salon_name = ""
branch_Set = ""
branchSet_1 = ""
def search(request):
    # salons = get_object_or_404() 
    query = request.GET.get("keyword")
    salon= Salon.objects.get(name__icontains=query)
    branchSet = SalonBranch_1.objects.filter(salonId=salon.salonId)
    salon_name = salon.name
    branch_Set = branchSet
    print "salon_name"+salon_name
    print branch_Set
    displayreview=Reviews_rating.objects.all()
    return render(request, "searchedresult.html",{"salon":salon.name,"branch":branchSet,"rev":displayreview})

def salonDetails(request):
    # salon = request.GET.get("salonId")
    branch = request.GET.get("branchId")

    # print "jggmntkgj"
    # salonObj = Salon.objects.get(pk=salon)
    searchset = SalonDetailsSingleDeals_1.objects.get(branchId=branch)
    searchset_1 = SalonDetailsComboDeals_1.objects.get(branchId=branch)
    return render(request, "salonDetails.html",{"salonDetails":searchset,"salonDetails1":searchset_1 })
    # return render(request, "salonDetails.html",{"salonDetails":searchset_1})

def suggestions(request):
    args = {}
    args.update(csrf(request))
    name = request.POST.get("Name")
    user_email = request.POST.get('User_email')
    postedquery = request.POST.get('Postedquery')
    if request.POST:
        form = ExpertForm(request.POST)
        if form.is_valid():
            form.save()
            html = "<html><body>Your query has been posted.We will get back to you shortly</body></html>"
            return HttpResponse(html)
    print name
    print user_email
    print postedquery
    html = "<html><body>Form Error</body></html>"
    return HttpResponse(html)
    

def suggestions1(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('suggestions.html', args)

def review(request):
    print "kdhais"
    args = {}
    args.update(csrf(request))
    name = request.POST.get("Name")
    Reviews = request.POST.get('reviews')
    branchid = request.POST.get('branchId')
    print name
    print Reviews
    print branchid
    if request.POST:
        form = Reviews_ratingForm(request.POST)
        if form.is_valid():
            print "hellooooooooooooooooooooooooooooooooooooooooooooooooooooo"
            form.save()
            displayreview=Reviews_rating.objects.all()
            return render(request, "searchedresult.html",{"salon":salon_name,"branch":branch_Set,"rev":displayreview})
        else:
            html = "<html><body>go to hell</body></html>"
            # return HttpResponse(html)