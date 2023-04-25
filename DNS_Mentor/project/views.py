from django.shortcuts import render
from .forms import MyForm
from .models import Mentor
from django.http import HttpResponse
from django.db.models import Q


# ментор
def mentor(request):
    return render(request, 'project/mentor.html')


# каталог
def catalog(request):
    search_query = request.GET.get('q', '')
    filters = request.GET.get('select', '')
    if filters:
        if search_query:
            mentors = Mentor.objects.filter(Q(mentor_surname__icontains=search_query) |
                                            Q(mentor_name__icontains=search_query) |
                                            Q(sphere__icontains=search_query) |
                                            Q(sphere__icontains=filters))
        else:
            mentors = Mentor.objects.filter(Q(sphere__icontains=filters))
    else:
        if search_query:
            mentors = Mentor.objects.filter(Q(mentor_surname__icontains=search_query) |
                                            Q(mentor_name__icontains=search_query) |
                                            Q(sphere__icontains=search_query))
        else:
            mentors = Mentor.objects.all()

    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            selected_options = form.cleaned_data.get('my_field')
            print(selected_options)

    context = {'mentors': mentors, 'form': form}
    return render(request, 'project/catalog.html', context)


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
