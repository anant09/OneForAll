from django.conf.urls import url 
from courier import views

urlpatterns = [ 
	url(r'^about/',views.about, name='about'),
	# url(r'^viewcourier/(?P<loc_from>[\w ]+)/(?P<loc_to>[\w ]+)/$',views.view_courier, name='view_courier'),
	# url(r'^viewcourier/(?P<loc_to>\w)/$', views.view_courier, name='view_courier'),
	url(r'^request_made/$', views.req_made, name='req_made'),
	url(r'^delete_courier/$', views.delete_courier, name='delete_courier'),

]
