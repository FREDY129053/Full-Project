from django.urls import path
from .views import *


# создание ссылок на страницы
urlpatterns = [
	path('', home),
	path('mentor.html/index.html', home),
	path('full/index.html', home),
	path('catalog/index.html', home),
	path('mentor/index.html', home),
	path('home_form/', home, name='home_form'),
	path('home_form/index.html', home),

	path('catalog.html', catalog),
	path('home_form/catalog.html', catalog),
	path('full/catalog.html', catalog),
	path('mentor.html/catalog.html', catalog),
	path('catalog/', catalog, name='catalog'),
	path('full/', catalog, name='full'),
	path('meeting/', catalog, name='meeting'),
	path('meeting/catalog.html', catalog),

	path('mentor.html/<int:mentor_id>', mentor, name='mentor'),
	path('mentor/', catalog, name='mentor_mentor'),
	# path('mentor.html', mentor),
]
