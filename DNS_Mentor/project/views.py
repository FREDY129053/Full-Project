import mysql

from mysql.connector import connect
from django.shortcuts import render
from .forms import MentorForm
from .models import Mentor
from django.http import HttpResponse
from django.db.models import Q
from django.db.models.query import QuerySet


# ментор
def mentor(request):
    return render(request, 'project/mentor.html')


# каталог
def catalog(request):
    search_query = request.GET.get('q', '')
    if search_query:
        mentors = Mentor.objects.filter(Q(mentor_surname__icontains=search_query) |
                                        Q(mentor_name__icontains=search_query) |
                                        Q(sphere__icontains=search_query))
    else:
        mentors = Mentor.objects.all()

    print(mentors)
    context = {'mentors': mentors}
    return render(request, 'project/catalog.html', context)


def postsearch(request):
    search = request.POST.get("search", "ALina")
    # return HttpResponse(f"<h2>{search}</h2>")
    print(search)


# домашняя страница
def home(request):
    return render(request, 'project/index.html')


# временная ссылка на анкету для ментора
def about(request):
    return render(request, 'project/a.html')


# не рабочая штука с анкетой пользователя
# def index(request):
#     if request.method == 'POST':
#         form = MentorForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             email = form.cleaned_data['email']
#             telegram = form.cleaned_data['first_name']
#             profession = form.cleaned_data['profession']
#             about_me = form.cleaned_data['about_me']
#         else:
#             form = MentorForm()
#         return render(request, 'mentor.html', {'form': form})
