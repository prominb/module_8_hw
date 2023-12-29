from datetime import date, datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    '''Ключ словника це дні тижня "Monday", "Tuesday", "Wednesday", "Thursday", "Friday".
    Значення це списки користувачів з днями народження на тиждень вперед від поточного дня, включаючи поточний день.'''

    '''Для прикладу, якщо я запускаю скрипт в середу, то в ключах "Wednesday", "Thursday", "Friday" дні народження цього тижня,
    а в ключах "Monday", "Tuesday" зберігаються дні народження наступного тижня. В ключі "Monday" завжди дні народження цього тижня які припали на вихідні.'''

    '''Код повинен бути чистим і дотримуватися стандартів PEP 8.'''

    # users_dict = dict() # {'Monday': ['Bill', 'Jan'], 'Wednesday': ['Kim']}
    # for i in range(7):
    #     d2 = datetime(year=2024, month=1, day=i+1) # , hour=8)
    #     # print(d2.strftime('%A'))
    #     list_of_names.append(d2.strftime('%A'))

    # print(type(list_of_names), list_of_names)
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']  # #####################
    # # days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') # tuple(list_of_names)
    # # print(type(days_of_week), days_of_week)
    list_of_names = list()  # #####################
    result_dict = dict.fromkeys(days_of_week, list_of_names)  # My result dictionary # ###################
    # print(result_dict) #########

    # result_dict_ver2 = defaultdict(list) # можна і так зробити словник
    # words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
    # grouped_words = defaultdict(list)
    # for day in days_of_week:
    #     char = day[0]
    #     result_dict_ver2[char].append(day)
    # print(result_dict_ver2)

    '''Функція повинна коректно працювати з порожнім списком користувачів.'''

    if not users:
    #     print(True, "Пусто")
    # else:
    #     print(False, "НЕ Пусто")
        return result_dict
        # return result_dict_ver2 ###################

    current_date = date.today()  # GET today date ########################
    # current_year = current_date.year #########################
    # current_datetime = datetime.now()
    # print(current_date, current_date.year, current_date.month, current_date.day, current_datetime)
    # d1 = datetime(year=current_date.year, month=current_date.month, day=current_date.day, hour=current_datetime.hour)
    # print(d1) # 2023-12-28 12:00:00
    current_day_of_week_2023 = datetime(year=current_date.year, month=current_date.month, day=current_date.day)  # , hour=current_datetime.hour)
    # #### Щоб дізнатися день тижня, можна скористатися методом weekday
    # print(current_day_of_week_2023.weekday())   # 3
    # ts = current_day_of_week_2023.timestamp()
    # print(ts)   # 1703764800.0
    # ts += 100_000
    # print(datetime.fromtimestamp(ts))   # 2023-12-29 15:46:40
    name_current_day_of_week_2023 = current_day_of_week_2023.weekday()
    # print(type(name_current_day_of_week_2023))
    name_current_day_of_week_2023 = current_day_of_week_2023.strftime('%A')
    # print(type(name_current_day_of_week_2023))
    # print(name_current_day_of_week_2023, name_current_day_of_week_2023 == 'Thursday')

    interval = timedelta(days=7)  # ##############
    # print(current_date + interval) ##
    next_week_person_birthday = current_date + interval  # ###################
    # current_day_111 = datetime.now()
    # # print(current_day_111)
    # interval = timedelta(days=7)
    # day_off = current_day_111-interval
    # print(day_off, day_off.weekday())
    # day_on = current_day_111+interval
    # print(day_on-day_off)


    # print(datetime.fromisoformat('20111104T000523')) # 2011-11-04 00:05:23 # # datetime.datetime(2011, 11, 4, 0, 5, 23)

    for person in users:
        # print(type(person), person)
        person_birthday = person['birthday']
        person_name = person['name']
        # print(type(person_birthday), person_birthday, person_name, type(person_name))
        current_person_birthday = datetime(year=current_date.year, month=person_birthday.month, day=person_birthday.day)
        print(current_person_birthday.date(), current_person_birthday.weekday(), person_name, person_birthday)
        # print(current_date.month, current_person_birthday.month)
        # person_birthday = person_birthday.replace(year=current_date.year + int(person_birthday.month == 1))  # ##### ?????????????????????
        # print(person_birthday)
        # if current_date.month == current_person_birthday.month and current_person_birthday.weekday() in (5, 6):
        #     result_dict['Monday'].append(person_name)

        # for key, value in person.items():
        #     # print(type(item), item)
        #     print(key, value)


    # #### RETURN RESULT OF FUNCTION ####
    users = result_dict.copy()
    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
        {"name": "Bruce Willis", "birthday": datetime(1955, 3, 19).date()},
        {"name": "Ryan Gosling", "birthday": datetime(1980, 11, 12).date()},
        {"name": "Jennifer Aniston", "birthday": datetime(1969, 2, 11).date()},
        {"name": "Robert Downey Jr.", "birthday": datetime(1965, 4, 4).date()},
        {"name": "Jeff Bridges", "birthday": datetime(1949, 12, 4).date()},
        {"name": "Scarlett Johansson", "birthday": datetime(1984, 11, 22).date()},
        {"name": "Chris Hemsworth", "birthday": datetime(1983, 8, 11).date()},
        {"name": "Tom Holland", "birthday": datetime(1996, 6, 1).date()},
        {"name": "Zoe Saldana", "birthday": datetime(1978, 6, 19).date()},
        {"name": "Chris Pratt", "birthday": datetime(1979, 6, 21).date()},
        {"name": "Josh Brolin", "birthday": datetime(1968, 2, 12).date()},
        {"name": "Kit Harington", "birthday": datetime(1986, 12, 26).date()},
        {"name": "Jude Law", "birthday": datetime(1972, 12, 29).date()},
    ]
    # users = [] # Check Empty list

    result = get_birthdays_per_week(users)
    print(result)
    # get_birthdays_per_week()
    # get_birthdays_per_week(users)
    # Виводимо результат
    # for day_name, names in result.items():
        # print(f"{day_name}: {', '.join(names)}")
