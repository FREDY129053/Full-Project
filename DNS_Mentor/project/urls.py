from django.urls import path
from .views import *


# создание ссылок на страницы
urlpatterns = [
	path('', catalog),
	path('about/', about),
	path('index/', index),
	path('mentor/', mentor),
	path('catalog/', catalog),
]
