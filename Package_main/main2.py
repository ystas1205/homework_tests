courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков",
     "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков",
     "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев",
     "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков",
     "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин",
     "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев",
     "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко",
     "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин",
     "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов",
     "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин",
     "Александр Иванов", "Антон Солонилин", "Максим Филипенко",
     "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер",
     "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая",
     "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]


def putting_things_in_order():
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor,
                       "duration": duration}
        courses_list.append(course_dict)
    durations_dict = {}
    for id, course in enumerate(courses_list):
        key = (course['duration'])
        durations_dict.update({id: key})

    durations_dict = dict(sorted(durations_dict.items(), key=lambda x: x[1]))

    #durations_dict = dict(sorted(durations_dict.items()))
    list_of_ordered_courses = []
    for key, value in durations_dict.items():
        list_of_ordered_courses.append(f'{courses[key]} - {value}')
    #print ((int(list_of_ordered_courses[0][-2:])))
    return list_of_ordered_courses


if __name__ == "__main__":
    print(putting_things_in_order())
