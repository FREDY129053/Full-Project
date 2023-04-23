from django.urls import path
from .views import *


# создание ссылок на страницы
urlpatterns = [
	path('', home),
	path('about/', about),
	path('index/', index),
	path('mentor/', mentor),
	path('catalog/', catalog),
]
