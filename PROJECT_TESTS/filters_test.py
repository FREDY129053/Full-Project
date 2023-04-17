from mysql.connector import connect, Error

try:
    with connect(
        host="193.124.118.138",
        user="me",
        password="password",
        database="project"
    ) as connection:
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)

        # Вывод значений таблицы и всех ее элементов
        select_mentors = "SELECT * FROM mentors"
        show_table = "DESCRIBE mentors"
        with connection.cursor() as cursor:
            cursor.execute(show_table)
            result = cursor.fetchall()
            for row in result:
                print(row)
            print()
            cursor.execute(select_mentors)
            result = cursor.fetchall()
            for row in result:
                print(row)

        print()

        # Ввод инфы для фильтра и поиска
        filt_category = input("Фильтровать по ")
        if filt_category == "sphere":
            print("Возможные значения:")
            select_spheres = f"SELECT {filt_category} FROM mentors"
            with connection.cursor() as cursor:
                cursor.execute(select_spheres)
                result = cursor.fetchall()
                # создание неповторяющихся значений фильтра у сфер
                temp = [i for sub in result for i in sub]
                temp2 = []
                for i in temp:
                    if "" in i:
                        temp2.append(i.split())
                    else:
                        temp2.append(i)
                temp3 = [i for sub in temp2 for i in sub]
                filters_values = set(temp3)
                for item in filters_values:
                    print(item)

            filt_value = input("Значение фильтра ")
            filt = f"""
            SELECT * FROM mentors
            WHERE {filt_category} LIKE '%{filt_value}%'
            """
        else:
            filt_value = input("Значение фильтра ")
            filt_more_less = input("Больше / меньше / равно ")
            filt = f"""
            SELECT * FROM mentors
            WHERE {filt_category} {filt_more_less} {filt_value}
            """
        search_input = input("Поиск ")
        search_input_list = search_input.split()

        # Вывод отфильтрованной информации
        with connection.cursor() as cursor:
            print(f"Фильтр по {filt_category}")
            cursor.execute(filt)
            for mentor in cursor.fetchall():
                print(mentor)

        # Вывод поиска
        with connection.cursor() as cursor:
            print("Результаты поиска:")
            search = "SELECT id, mentor_telegram, mentor_surname, mentor_name, sphere FROM mentors"
            cursor.execute(search)
            mentor_search_list = cursor.fetchall()
            for mentor in mentor_search_list:
                ment = str(mentor)
                ment = ment.lower()
                i = 1
                id = ""
                replace = "("
                while ment[i] != ',':
                    replace += ment[i]
                    id += ment[i]
                    i += 1
                replace += ', '
                ment = ment.replace(replace, '(', 1)
                for j in search_input_list:
                    j = j.lower()
                    if ment.find(j) > -1:
                        mentor_found = f"""
                        SELECT * FROM mentors
                        WHERE id = {id}
                        """
                        cursor.execute(mentor_found)
                        print(cursor.fetchall()[0])
                        break
            search_input_list.clear()
except Error as e:
    print(e)

