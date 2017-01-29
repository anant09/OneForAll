from django.conf.urls import url 
from tickets import views

urlpatterns = [ 
	url(r'^view_all/',views.view_all, name='view_all'),
	# url(r'^viewcourier/(?P<loc_from>[\w ]+)/(?P<loc_to>[\w ]+)/$',views.view_courier, name='view_courier'),
	# url(r'^viewcourier/(?P<loc_to>\w)/$', views.view_courier, name='view_courier'),
	# url(r'^request_made/$', views.req_made, name='req_made'),
	url(r'^fetch_data/',views.fetch_data, name='fetch_data'),
	url(r'^fetch_courier/',views.fetch_couriers, name='fetch_couriers'),
	# url(r'^delete_courier/$', views.delete_courier, name='delete_courier'),
]
