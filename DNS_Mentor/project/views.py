from django.shortcuts import render
from django.http import HttpResponse
from .forms import MentorForm


# ментор
def mentor(request):
    return render(request, 'project/mentor.html')


# каталог
def catalog(request):
    # return render(request, 'project/catalog — old.html')
    return render(request, 'project/catalog.html')


def postsearch(request):
    search = request.POST.get("search", "Undefined")
    return render(request, 'project/catalog.html')


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
