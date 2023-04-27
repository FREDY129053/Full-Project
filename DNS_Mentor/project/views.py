import mysql

from PIL import Image
from io import BytesIO
from mysql.connector import connect
from django.shortcuts import render, get_object_or_404
from .models import Mentor
from .forms import MentorForm, UserForm
from django.http import HttpResponse
from django.db.models import Q

# global MySQL vars
db_config = {
        "user": "me",
        "password": "password",
        "host": "193.124.118.138",
        "database": "project",
    }
db = mysql.connector.connect(**db_config)
cursor = db.cursor(buffered=True)


# ментор
def mentor(request, mentor_id):
    person = get_object_or_404(Mentor, id=mentor_id)

    return render(request, 'project/mentor.html', {'person': person})


# каталог
def catalog(request):

    cursor.execute("SELECT sphere FROM mentors")
    options = cursor.fetchall()

    temp = [i for sub in options for i in sub]
    temp2 = []
    temp3 = []
    for i in temp:
        temp2.append(i.split(","))

    for i in temp2:
        for j in i:
            temp3.append(j)

    form1 = MentorForm()
    form2 = UserForm()
    if request.method == 'POST':
        form1 = MentorForm(request.POST)
        form2 = UserForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            name = form1.cleaned_data['first_name']
            surname = form1.cleaned_data['last_name']
            mail = form1.cleaned_data['email']
            tg = form1.cleaned_data['telegram'] if '@' in form1.cleaned_data['telegram'] else '@' + form1.cleaned_data['telegram']
            price = form1.cleaned_data['price']
            exp = int(form1.cleaned_data['exp'])
            sphere = form1.cleaned_data['profession']
            about_mentor = form1.cleaned_data['about_me']

            user_name = form2.cleaned_data['user_name']
            user_surname = form2.cleaned_data['user_surname']
            user_email = form2.cleaned_data['user_email']
            user_telegram = form2.cleaned_data['user_telegram'] if '@' in form2.cleaned_data['user_telegram'] else '@' + form2.cleaned_data['user_telegram']
            meet_date = form2.cleaned_data['meeting_date']
            mentor_tg = form2.cleaned_data['mentor_tg']

            cursor.execute(f"INSERT INTO applications_for_mentoring(surname, name, telegram, mail, price, experience, sphere, about) "
                           f"VALUES('{surname}', '{name}', '{tg}', '{mail}', '{price}', {exp}, '{sphere}', '{about_mentor}')")
            db.commit()

            cursor.execute(
                f"INSERT INTO applications_for_meeting(user_surname, user_name, mentor_telegram, user_telegram, date_of_meeting, user_mail "
                f"VALUES('{user_surname}', '{user_name}', '{mentor_tg}', '{user_telegram}', '{meet_date}', '{user_email}')")
            db.commit()



        else:
            if form1.is_valid():
                name = form1.cleaned_data['first_name']
                surname = form1.cleaned_data['last_name']
                mail = form1.cleaned_data['email']
                tg = form1.cleaned_data['telegram'] if '@' in form1.cleaned_data['telegram'] else '@'+form1.cleaned_data['telegram']
                price = form1.cleaned_data['price']
                exp = int(form1.cleaned_data['exp'])
                sphere = form1.cleaned_data['profession']
                about_mentor = form1.cleaned_data['about_me']

                cursor.execute(f"INSERT INTO applications_for_mentoring(surname, name, telegram, mail, price, experience, sphere, about) "
                               f"VALUES('{surname}', '{name}', '{tg}', '{mail}', '{price}', {exp}, '{sphere}', '{about_mentor}')")
                db.commit()


            if form2.is_valid():
                user_name = form2.cleaned_data['user_name']
                user_surname = form2.cleaned_data['user_surname']
                user_email = form2.cleaned_data['user_email']
                user_telegram = form2.cleaned_data['user_telegram'] if '@' in form2.cleaned_data['user_telegram'] else '@'+form2.cleaned_data['user_telegram']
                meet_date = form2.cleaned_data['meeting_date']
                mentor_tg = form2.cleaned_data['mentor_tg']

                cursor.execute(f"INSERT INTO applications_for_meeting(user_surname, user_name, mentor_telegram, user_telegram, date_of_meeting, user_mail) VALUES('{user_surname}', '{user_name}', '{mentor_tg}', '{user_telegram}', '{meet_date}', '{user_email}')")
                db.commit()


    filters_values = set(temp3)
    filters_values = [i.lstrip() for i in filters_values]

    search_query = request.GET.get('q', '')
    filters_query = request.GET.getlist('select', '')

    search_query = search_query.split(' ')
    mentors = Mentor.objects.all()

    spheres = []
    temp_spheres = [i.lstrip() for i in filters_values]
    experiences = []
    temp_experiences = ["Junior", "Middle", "Senior"]
    prices_str = []
    prices_int = []
    temp_prices = ["Undefined", "Free", "Low", "Medium", "High"]

    for i in temp_spheres:
        if i in filters_query:
            spheres.append(i)

    for i in temp_experiences:
        if i in filters_query:
            if i == "Junior":
                experiences.append(0)
                experiences.append(2)
            elif i == "Middle":
                experiences.append(3)
                experiences.append(5)
            elif i == "Senior":
                experiences.append(6)
                experiences.append(1000000000000)

    for i in temp_prices:
        if i not in filters_query:
            if i == "Undefined":
                prices_str.append("по договоренности")
            elif i == "Free":
                prices_str.append("бесплатно")
            elif i == "Low":
                prices_int.append(0)
                prices_int.append(2999)
            elif i == "Medium":
                prices_int.append(3000)
                prices_int.append(5999)
            elif i == "High":
                prices_int.append(6000)
                prices_int.append(1000000000000)
    if len(prices_str) == 2 and len(prices_int) == 6:
        prices_str.clear()
        prices_int.clear()

    if filters_query:
        if spheres:
            spheres_q = Q()
            for i in spheres:
                spheres_q |= Q(sphere__icontains=i)
            mentors = mentors.filter(spheres_q)

        if experiences:
            experiences_q = Q()
            for i in range(0, len(experiences), 2):
                experiences_q |= Q(experience__range=(experiences[i], experiences[i + 1]))
            mentors = mentors.filter(experiences_q)

        for i in prices_str:
            mentors = mentors.exclude(price__icontains=i)
        for i in range(0, len(prices_int), 2):
            mentors = mentors.exclude(price__range=(prices_int[i], prices_int[i + 1]))

    if search_query:
        for i in search_query:
            mentors = mentors.filter(Q(mentor_surname__icontains=i) |
                                     Q(mentor_name__icontains=i) |
                                     Q(sphere__icontains=i))

    context = {'mentors': mentors, 'options': filters_values, 'form1': form1, 'form2': form2}
    return render(request, 'project/catalog.html', context)


# домашняя страница
def home(request):
    form = MentorForm()
    if request.method == 'POST':
        form = MentorForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['first_name']
            surname = form.cleaned_data['last_name']
            mail = form.cleaned_data['email']
            tg = form.cleaned_data['telegram']
            price = form.cleaned_data['price']
            exp = int(form.cleaned_data['exp'])
            sphere = form.cleaned_data['profession']
            about_mentor = form.cleaned_data['about_me']


            cursor.execute(f"INSERT INTO applications_for_mentoring(surname, name, telegram, mail, price, experience, sphere, about) VALUES('{surname}', '{name}', '{tg}', '{mail}', '{price}', {exp}, '{sphere}', '{about_mentor}')")
            db.commit()


    return render(request, 'project/index.html', {'form': form})
