from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.inicio), #^$ siempre es importante ponerlo en tu template de inicio
	url(r'^registro/$', views.registro), #aqui vas las views al final siempre poner un slash, siempre debe llevar el ^ al principio y /$ al final

]