from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from courier.models import *
from .models import *
from models import User
import json
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
# Create your views here.

    
    
@login_required 
def view_all(request):
    all_tickets={'boldmessage': Tickets.objects.all() }
    return render(request,'tickets/view_tickets.html',context=all_tickets)
@login_required   
def fetch_data(request):
	if request.method == 'POST':
		journey = request.POST['train']
		for items in Tickets.objects.filter(journey_id=journey):
			# print items
			source = items.location_from
			destination = items.location_to
			couriers={'courier': Courier.objects.filter(location_from=source,location_to=destination)}
			print couriers
			return render(request,'tickets/print_courier.html',context=couriers)

@login_required
def fetch_couriers(request):
        if request.method == 'POST':
            checked = request.POST.getlist('cpackage')
            for items in checked:
                  q=Tracker(user=request.user.username,courier_details=items)
                  for mi in Courier.objects.filter(id=items):
                      em=[mi.user.email]
                      print 'lalala '
                      print em
                      subject2='Courier Accepted'
                      subject='Confirmation mail'
                      message2='Your courier with the courier id '+ str(mi.id)+' has been accepted to be delivered.\n The tracking address will be provided soon'
                      message='You have agreed to deliver courier of weight:-'+str(mi.weight)
                      print message
                      from_email = settings.EMAIL_HOST_USER
                      to_list = [request.user.email]
                      print "a aaaaaaaaaa"
                      print to_list
                      send_mail(subject,message,from_email,to_list,fail_silently = True)
                      send_mail(subject2,message2,from_email,em,fail_silently=True)
                  q.save()
        return HttpResponseRedirect('/home/')

@login_required
def delete_courier(request):
    if request.method=='POST':
        print "post"
        checked = request.POST.getlist('cpackage')
        for items in checked:
            Tracker.objects.filter(courier_details=items).delete()
        return HttpResponseRedirect('/home  ')
    else:
        # dict={'courier':Tracker.objects.filter(user=request.user.username)}
        couriers=[]
        dict = {}
        for items in Tracker.objects.filter(user=request.user.username):
        	# print items
        	couriers.append(Courier.objects.filter(id=items.courier_details)[0])
        print couriers
        dict['courier'] = couriers
        	# print Courier.objects.filter(id=items.courier_details)

        return render(request,'tickets/delete_courier.html',context=dict)


		# q = Tracker(user =request.user.username,train_details=requ
# def about(request):
# 	# if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         # form = NameForm(request.POST)
#         # check whether it's valid:
#         print "post variables", request.POST
#         print "entered post"
#         # if form.is_valid():
#         q= Courier(user=request.user, weight=request.POST['weight'],height=request.POST['height'],width=request.POST['width'],length=request.POST['length'],location_from=request.POST['location_from'],location_to=request.POST['location_to'])
#         subject = 'Landbnb order'
#         message = 'Your order has been recorded successfully. Please notify if any of the following details are incorrect or need to be changed:- \nWeight :'+ str(request.POST['weight'])+'\nHeight: '+str(request.POST['height'])+'\nWidth: '+str(request.POST['width'])+'\nLength: '+str(request.POST['length'])+'\nFrom: '+str(request.POST['location_from'])+'\nDestination: '+str(request.POST['location_to'])
#         from_email = settings.EMAIL_HOST_USER
#         to_list = [request.user.email]

#         send_mail(subject,message,from_email,to_list,fail_silently = True)
#         q.save()
#         return HttpResponseRedirect('/courier/request_made/')
#         # else:
#             # print "errors",form.errors
            
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         # form = NameForm()
#         user = request.user

#     return render(request, 'courier/welcome.html', {'user':request.user})
# # Create your views here.
