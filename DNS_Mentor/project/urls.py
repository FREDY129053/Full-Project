from django.urls import path
from .views import *


# создание ссылок на страницы
urlpatterns = [
	path('', home),
	path('about/', about),
	path('mentor/', mentor),
	path('catalog/', catalog, name='catalog'),
	path('index.html', home),
	path('catalog.html', catalog),
	path('mentor.html', mentor),
]
