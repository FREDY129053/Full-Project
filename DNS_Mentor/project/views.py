import mysql

from mysql.connector import connect
from django.shortcuts import render
from .forms import MentorForm
from django.http import HttpResponse


# ментор
def mentor(request):
    return render(request, 'project/mentor.html')


# каталог
def catalog(request):
    db_config = {
        "user": "me",
        "password": "password",
        "host": "193.124.118.138",
        "database": "project",
    }
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor(buffered=True)

    cursor.execute("SELECT * FROM mentors ORDER BY id ASC")
    mentors = cursor.fetchall()

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
def index(request):
    if request.method == 'POST':
        form = MentorForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            telegram = form.cleaned_data['first_name']
            profession = form.cleaned_data['profession']
            about_me = form.cleaned_data['about_me']
        else:
            form = MentorForm()
        return render(request, 'mentor.html', {'form': form})
