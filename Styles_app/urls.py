from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('Styles_app.views',
	url(r'^$', views.first, name = 'first'),
	url(r'^Styles/$', views.first, name='first'),
	url(r'^index1/$', views.index1, name='index1'),
	url(r'^login/$', views.login, name='login'),
	url(r'^login_check/$', views.login_check, name='login_check'),
	url(r'^registration/$', views.registration, name='registration'),
	url(r'^registration_check/$', views.registration_check, name='registration_check'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^otp/$', views.otp, name='otp'),
	url(r'^otpcheck/$', views.otpcheck, name='otpcheck'),
	url(r'^about', views.about, name = 'about'),
	url(r'^contact', views.contact, name = 'contact'),
	url(r'^search/$', views.search, name = 'search'),
	url(r'^salonDetails/$', views.salonDetails, name = 'salonDetails'),
	url(r'^suggestions/$', views.suggestions, name = 'suggestions'),
	url(r'^suggestions1/$', views.suggestions1, name = 'suggestions1'),
	url(r'^review/$', views.review, name = 'review'),
	)
