from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='project-home'),
	path('about/', views.about, name='about-club'),
	path('index/', views.index, name='mentor'),
]