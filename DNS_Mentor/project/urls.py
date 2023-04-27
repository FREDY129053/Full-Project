from django.urls import path
from .views import *


# создание ссылок на страницы
urlpatterns = [
	path('', home),
	path('about/', about),
	# path('mentor/', mentor, name='mentor'),
	path('catalog/', catalog, name='catalog'),
	path('mentor.html/index.html', home),
	path('mentor.html/<int:mentor_id>', mentor, name='mentor'),
	path('catalog.html', catalog),
	path('mentor.html/catalog.html', catalog),
	path('mentor.html', mentor),
	path('full/', catalog, name='full')
]
