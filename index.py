# ПРОСТЕЙШИЕ ОПЕРАЦИИ С ПЕРЕМЕННЫМИ
# Задание 1
# Калькулятор возраста питомца
# Создайте программу, которая:
# Сохраняет в переменную  human_years  возраст человека (например,
# 5)
# Сохраняет в переменную  animal_type  тип животного ("собака" или
# "кошка")
# Рассчитывает возраст животного в "человеческих" годах:
# Для собак: первый год = 15 человеческих лет, второй год = 9 лет,
# каждый следующий = 5 летДля кошек: первый год = 15 лет, второй год = 10 лет, каждый
# следующий = 4 года
# Выводит результат в формате: "Возраст {животное} в человеческих
# годах: {результат}"
# human_years = 11
# animal_type = "кошка"
# if animal_type == "собака":
#     if human_years == 1:
#         animal_age = 15
#     elif human_years == 2:
#         animal_age = 15 + 9
#     else:
#         animal_age = 15 + 9 + (human_years - 2) * 5
# if animal_type == "кошка":
#     if human_years == 1:
#         animal_age = 15
#     elif human_years == 2:
#         animal_age = 15 + 10
#     else:
#         animal_age = 15 + 10 + (human_years - 2) * 4
# print(f"Возраст питомца ({animal_type}) в человеческих годах: {animal_age}")

# Задание 2
# Напишите программу для конвертации рублей в другие валюты:
# Создайте переменную  rubles  с суммой в рублях (например, 5000)
# Создайте переменные с курсами валют:  usd_rate = 90.5 ,  eur_rate
# = 98.2 ,  cny_rate = 12.3
# Рассчитайте и выведите:
# Сколько долларов можно купитьСколько евро можно купитьСколько юаней можно купить
# Результат округлите до 2 знаков после запятой
# rubles = 5000
# usd_rate = 90.5
# eur_rate = 98.2
# cny_rate = 12.3
# print(f'На сумму {rubles} вы можете купить:')
# print(f'- долларов США: {rubles / usd_rate: .2f}')
# print(f'- евро: {rubles / eur_rate: .2f}')
# print(f'- юаней: {rubles/cny_rate: .2f}')

# Задание 3
# Калькулятор времени
# Создайте программу, которая переводит секунды в часы, минуты и
# секунды:
# Сохраните в переменную  total_seconds  количество секунд
# (например, 3665)
# Рассчитайте:
# Количество полных часов Остаток минут Остаток секунд 
# Выведите результат в формате: "Это составляет X часов, Y минут, Z секунд"
# total_seconds = 3665
# hours = total_seconds // 3600
# rest_after_hours = total_seconds % 3600
# minutes = rest_after_hours // 60
# seconds = rest_after_hours % 60
# print(f'{total_seconds} сек. - это: {hours} час. {minutes} мин. {seconds} сек.')

# Задание 4
# Магазин скидок
# Напишите программу расчета итоговой цены:
# Создайте переменные:  price  (цена товара),  quantity
# (количество),  has_discount_card  (есть ли карта скидки)
# Если количество > 5, применяется скидка 10%
# Если есть карта скидки, применяется дополнительная скидка 5%
# Рассчитайте итоговую сумму с учетом всех скидок
# Выведите исходную сумму, сумму каждой скидки и итоговую цену
# price = 1000
# quantity = 5
# has_discount_card = True
# initial_price = price * quantity
# discount_quantity = 0
# discount_card = 0
# if quantity > 5 and has_discount_card:
#     discount_quantity = initial_price * 0.1
#     discount_card = initial_price * 0.05
#     total_price = initial_price - discount_quantity - discount_card
#     print(f'Исходная сумма: {initial_price} руб.')
#     print(f'Скидка за количество (10%): {discount_quantity} руб.')
#     print(f'Скидка по карте (5%): {discount_card} руб.')
#     print(f'Итоговая цена: {total_price} руб.')
# elif quantity > 5:
#     discount_quantity = initial_price * 0.1
#     total_price = initial_price - discount_quantity
#     print(f'Исходная сумма: {initial_price} руб.')
#     print(f'Скидка за количество (10%): {discount_quantity} руб.')
#     print(f'Итоговая цена: {total_price} руб.')
# elif has_discount_card:
#     discount_card = initial_price * 0.05
#     total_price = initial_price - discount_card
#     print(f'Исходная сумма: {initial_price} руб.')
#     print(f'Скидка по карте (5%): {discount_card} руб.')
#     print(f'Итоговая цена: {total_price} руб.')
# else:
#     print(f'Исходная сумма: {initial_price} руб.')
#     print(f'Итоговая цена: {initial_price} руб.')

# Задание 5
# BMI калькулятор (Индекс массы тела)
# Создайте программу для расчета индекса массы тела:
# Сохраните в переменные:  weight_kg  (вес в кг) и  height_m  (рост в
# метрах)
# Рассчитайте BMI по формуле: вес / (рост²)
# Определите категорию:< 18.5: "Недостаточный вес"
# 18.5 - 24.9: "Нормальный вес"
# 25 - 29.9: "Избыточный вес"
# >= 30: "Ожирение"
# Выведите результат: "Ваш BMI: {значение}, категория: {категория}"
# weight_kg = 47.5
# height_m = 1.60
# category = ''
# bmi = round(weight_kg / height_m ** 2, 1)
# if bmi < 18.5:
#     category = 'Недостаточный вес'
# elif 18.5 <= bmi <= 24.9:
#     category = 'Нормальный вес'
# elif 25 <= bmi <= 29.9:
#     category = 'Избыточный вес'
# elif bmi >= 30:
#     category = 'Ожирение'
# print(f'Ваш BMI: {bmi}, категория: {category}')

# УСЛОВНЫЙ ОПЕРАТОР
# Задание 1
# Определитель времени суток
# Напишите программу, которая определяет время суток по введенному
# часу:
# Сохраните в переменную  hour  текущий час (от 0 до 23)
# Используя условный оператор, определите:0-5: "Ночь"6-11: "Утро"12-17: "День"18-23: "Вечер"
# Выведите сообщение: "Сейчас {время_суток}"
# Дополнительно: Добавьте проверку, что час введен корректно (от 0 до 23)
# hour = input('Введите число от 0 до 23: ')
# time_of_day = ''
# if hour.isdigit():
#     hour = int(hour)
#     if 0 <= hour <= 23:
#         if 0 <= hour <= 5:
#             time_of_day = 'ночь'
#         elif 6 <= hour <= 11:
#             time_of_day = 'утро'
#         elif 12 <= hour <= 17:
#             time_of_day = 'день'
#         elif 18 <= hour <= 23:
#             time_of_day = 'вечер'
#         print(f'Сейчас {time_of_day}')
#     else:
#         print('Введите число от 0 до 23!')
# else:
#     print('Ошибка! Введите целое число!')

# Задание 2
# Калькулятор оценок
# Создайте программу для определения оценки по баллам:
# Создайте переменную  score  с количеством баллов (от 0 до 100)
# Используя if-elif-else, определите оценку:90-100: "Отлично (5)"75-89: "Хорошо (4)"50-74: "Удовлетворительно (3)"0-49: "Неудовлетворительно (2)"
# Выведите результат и дополнительное сообщение:
# Если баллы >= 90: "Поздравляю с отличным результатом!"
# Если баллы < 50: "Нужно подтянуть знания!"
# 1-й вариант
# score = input('Введите ваше количество баллов: ')

# if score.replace('.', '', 1).isdigit():
#     score = float(score)
    
#     if 0 <= score <= 100:
#         if score >= 90:
#             grade = 'Отлично (5)'
#             print(f'Ваша оценка: {grade}')
#             print('Поздравляю с отличным результатом!')
#         elif score >= 75:
#             grade = 'Хорошо (4)'
#             print(f'Ваша оценка: {grade}')
#         elif score >= 50:
#             grade = 'Удовлетворительно (3)'
#             print(f'Ваша оценка: {grade}')
#         else:
#             grade = 'Неудовлетворительно (2)'
#             print(f'Ваша оценка: {grade}')
#             print('Нужно подтянуть знания!')
#     else:
#         print('Ошибка! Введите число от 0 до 100!')
# else:
#     print('Ошибка! Введите число (можно с точкой)!')

# 2-й вариант 
# try:
#     score = float(input('Введите ваше количество баллов: '))
#     if 0 <= score <= 100:
#         if score >= 90:
#             grade = 'Отлично (5)'
#             print(f'Ваша оценка: {grade}')
#             print('Поздравляю с отличным результатом!')
#         elif score >= 75:
#             grade = 'Хорошо (4)'
#             print(f'Ваша оценка: {grade}')
#         elif score >= 50:
#             grade = 'Удовлетворительно (3)'
#             print(f'Ваша оценка: {grade}')
#         else:
#             grade = 'Неудовлетворительно (2)'
#             print(f'Ваша оценка: {grade}')
#             print('Нужно подтянуть знания!')
#     else:
#         print('Ошибка! Введите число от 0 до 100!')
# except ValueError:
#     print('Ошибка! Введите число (можно с точкой)!')

# Задание 3
# Треугольник или нет?
# Напишите программу, которая проверяет, можно ли построить
# треугольник с заданными сторонами:
# Создайте переменные  a ,  b ,  c  с длинами сторон
# Проверьте условие существования треугольника:
# Каждая сторона должна быть меньше суммы двух других
# Все стороны должны быть положительными
# Если треугольник существует, определите его тип:
# Все стороны равны: "Равносторонний"
# Две стороны равны: "Равнобедренный"
# Все стороны разные: "Разносторонний"
# Выведите соответствующий результат
# a = 2
# b = 3
# c = 4
# type_of_triangle = ''
# if a > 0 and b > 0 and c > 0:
#     if a < b + c and b < a + c and c < a + b:
#         if a == b == c:
#             type_of_triangle = 'равносторонний'
#         elif a == b or a == c or b == c:
#             type_of_triangle = 'равнобедренный'
#         else:
#             type_of_triangle = 'разносторонний'
#         print(f'Вы построили {type_of_triangle} треугольник')
#     else:
#         print('С такими сторонами треугольник не существует!')
# else:
#     print('Стороны не могут быть отрицательными!')

# Задание 4
# Счастливый билет
# Создайте программу для проверки "счастливого" билета:
# Сохраните в переменную  ticket_number  шестизначное число
# (например, 123456)
# Разделите число на первые три и последние три цифры
# Посчитайте сумму цифр первой половины и второй половины
# Используя условный оператор, проверьте:
# Если суммы равны: "Ура! Это счастливый билет!"
# Если разница сумм = 1: "Почти счастливый!"
# Иначе: "Обычный билет"
# Выведите обе суммы для наглядности
# ticket_number = input('Введите шестизначное число: ')
# if ticket_number.isdigit():
#     if len(ticket_number) == 6:
#         ticket_number = int(ticket_number)
#         first_half = ticket_number // 1000
#         second_half = ticket_number % 1000
#         sum1 = 0
#         sum2 = 0
#         for digit in str(first_half):
#             sum1 += int(digit)
#         for digit in str(second_half):
#             sum2 += int(digit)
#         print(f"Сумма первой половины: {sum1}")
#         print(f"Сумма второй половины: {sum2}")
#         if sum1 == sum2:
#             print('Ура! Это счастливый билет!')
#         elif abs(sum1 - sum2) == 1:
#             print('Почти счастливый!')
#         else:
#             print('Обычный билет')
#     else:
#         print(f'Необходимо ввести 6 цифр, а вы ввели {len(ticket_number)}!')
# else:
#     print('Введите число!')

# Задание 5
# Генератор советов по погоде
# Напишите программу, которая дает советы по погоде:
# Создайте переменные:
# temperature  (температура в градусах)
# is_raining  (булево значение, идет ли дождь)
# is_windy  (булево значение, ветрено ли)
# have_umbrella  (есть ли зонт)
# Используя вложенные условия и логические операторы (and, or, not),
# определите совет:
# Если температура < 0: "Очень холодно, одевайтесь теплее!"
# Если 0-15 и идет дождь и ветер: "Сыро и ветрено, лучше остаться
# дома"
# Если 15-25 и не идет дождь: "Отличная погода для прогулки!"
# Если > 25 и не идет дождь: "Жарко, не забудьте головной убор"
# Если идет дождь и есть зонт: "Можно идти, зонт спасет"
# Если идет дождь и нет зонта: "Лучше переждать дождь дома"
# Выведите персонализированный совет
# temperature = 18
# is_raining = False
# is_windy = True
# have_umbrella = False

# if temperature < 0:
#     print('Очень холодно, одевайтесь теплее!')
# elif 0 <= temperature <= 15 and is_raining and is_windy:
#     print('Сыро и ветрено, лучше остаться дома')
# elif 15 <= temperature <= 25 and not is_raining:
#     print('Отличная погода для прогулки!')
# elif temperature > 25 and not is_raining:
#     print('Жарко, не забудьте головной убор')
# elif is_raining and have_umbrella:
#     print('Можно идти, зонт спасет')
# elif is_raining and not have_umbrella:
#     print('Лучше переждать дождь дома')

# ЗАДАНИЯ ДЛЯ КАЖДОГО ТИПА ДАННЫХ В PYTHON
# Строки
# Напишите программу для анализа введенного текста:
# Сохраните в переменную  text  произвольную строку (например,"Программирование на Python - это интересно и полезно!")
# Выполните следующие операции:
# Подсчитайте количество символов (с пробелами и без)
# Найдите самое длинное слово в тексте
# Замените все пробелы на символ подчеркивания
# Проверьте, является ли текст палиндромом (игнорируя пробелы и регистр)
# Выведите текст в обратном порядке
# Результат каждой операции выведите отдельно
# import string
# text = 'Программирование на Python - это интересно и полезно!'

# # Создаем функцию для поиска самого длинного слова в тексте
# def longest_word(s):
#     words = s.split()  # Создаем список слов текста
#     clean_words = []
    
#     for word in words:
#         # Удаляем знаки препинания с начала и конца каждого слова
#         clean_word = word.strip(string.punctuation)
#         clean_words.append(clean_word)
    
#     # Находим самое длинное слово
#     longest = max(clean_words, key=len)
#     return longest

# # Создаем функцию проверки на палиндром
# def is_palindrom(s):
#     # Приводим все символы строки к нижнему регистру
#     lower_reg = s.lower()

#     # Убираем пробелы
#     no_spaces = lower_reg.replace(' ', '')

#     # Убираем все знаки препинания
#     table = str.maketrans('', '', string.punctuation)
#     clean_text = no_spaces.translate(table)

#     return clean_text == clean_text[::-1]



# print(f'Количество символов с пробелами: {len(text)}')

# print(f'Количество символов без пробелов: {len(text.replace(' ', ''))}')

# print(f'Самое длинное слово в тексте: {longest_word(text)}')

# print(text.replace(' ', '_'))

# if is_palindrom(text):
#     print((f'{text} - палиндром'))
# else:
#     print(f'{text} - не является палиндромом')

# print(text[::-1])

# Списки
# Задание: Управление списком покупок
# Создайте программу для работы со списком покупок:
# Создайте список  shopping_list  с товарами: ["хлеб", "молоко", "яйца",
# "сыр", "помидоры"]
# Выполните следующие действия:
# Добавьте в список "огурцы" и "колбасу"
# Удалите из списка "сыр"
# Замените "помидоры" на "перец"
# Отсортируйте список в алфавитном порядке
# Выведите количество элементов в списке
# Выведите первые 3 товара из списка
# После каждого изменения выводите текущий список
# shopping_list = ["хлеб", "молоко", "яйца", "сыр", "помидоры"]

# # Добавляем в список "огурцы" и "колбасу"
# shopping_list.append("огурцы")
# shopping_list.append("колбаса")
# print(shopping_list)

# # Удаляем из списка "сыр"
# shopping_list.remove("сыр")
# print(shopping_list)

# # Заменяем "помидоры" на "перец"
# shopping_list = [word.replace("помидоры", "перец") for word in shopping_list]
# print(shopping_list)

# # Сортируем список в алфавитном порядке
# shopping_list.sort()
# print(shopping_list)

# # Выводим количество элементов в списке
# print(f'Количество элементов в списке: {len(shopping_list)}')

# # Выводим первые 3 товара из списка
# print(shopping_list[:3])

# Множества
# Задание: Анализ подписчиков
# Напишите программу для анализа подписчиков в соцсетях:
# Создайте три множества:
# instagram_friends = {"Анна", "Петр", "Мария", "Иван",
# "Елена"}
# vk_friends = {"Петр", "Дмитрий", "Елена", "Ольга",
# "Сергей"}
# telegram_friends = {"Анна", "Сергей", "Елена", "Михаил",
# "Ирина"}
# Выполните операции:
# Найдите друзей, которые есть во всех трех соцсетях (пересечение)
# Найдите уникальных друзей в Instagram (которых нет в других сетях)
# Найдите друзей, которые есть хотя бы в одной соцсети (объединение)
# Проверьте, есть ли друг "Алексей" хотя бы в одной соцсети
# Выведите результаты каждой операции
# instagram_friends = {"Анна", "Петр", "Мария", "Иван", "Елена"}
# vk_friends = {"Петр", "Дмитрий", "Елена", "Ольга", "Сергей"}
# telegram_friends = {"Анна", "Сергей", "Елена", "Михаил", "Ирина"}
# check_name = "Алексей"

# # Создаем необходимые функции для проверки
# def get_common_friends(set1, set2, set3):
#     return set1 & set2 & set3

# def get_unique_instagram_friends(inst, vk, telegram):
#     return inst - vk - telegram

# def get_all_friends(set1, set2, set3):
#     return set1 | set2 | set3

# def is_friend_exists(all_friends, name):
#     return name in all_friends

# # Производим вывод результатов
# common_friends = get_common_friends(instagram_friends, vk_friends, telegram_friends)
# common_friends_list = list(common_friends)
# common_friends_list.sort()
# print(f'Друзья, которые есть во всех трех соцсетях: {', '.join(common_friends_list)}')

# unique_friends = get_unique_instagram_friends(instagram_friends, vk_friends, telegram_friends)
# unique_friends_list = list(unique_friends)
# unique_friends_list.sort()
# print(f'Уникальные друзья в Instagram: {', '.join(unique_friends_list)}')

# all_friends = get_all_friends(instagram_friends, vk_friends, telegram_friends)
# all_friends_list = list(all_friends)
# all_friends_list.sort()
# print(f'Друзья, которые есть хотя бы в одной социальной сети: {', '.join(all_friends_list)}')

# check_friend = is_friend_exists(all_friends, check_name)

# if check_friend:
#     print(f'{check_name} есть хотя бы в одной социальной сети')
# else:
#     print(f'{check_name} не найден ни в одной социальной сети')

# *Словари (Dictionaries)*
# Задание: Телефонный справочник
# Создайте программу для работы с телефонным справочником:
# Создайте словарь  phonebook :
# phonebook = {  "Иванов": "123-45-67",  "Петров": "234-56-78",  "Сидорова": "345-67-89"}
# Выполните операции:
# Добавьте новый контакт "Смирнов" с телефоном "456-78-90"
# Измените телефон Петрова на "999-99-99"
# Удалите контакт Сидоровой
# Проверьте, есть ли в справочнике контакт "Иванов"
# Выведите все контакты в формате "Фамилия: телефон"
# Найдите контакт по номеру телефона (введите "234-56-78")
# Каждое действие должно сопровождаться выводом результата
# phonebook = {
#     "Иванов": "123-45-67",  
#     "Петров": "234-56-78",  
#     "Сидорова": "345-67-89"
#     }

# # Создаем функцию добавления нового контакта
# def download_contact(dictionary, key, value):
#     dictionary.setdefault(key, value)
#     return dictionary

# # Создаем функцию изменения номера телефона
# def to_change_phone(dictionary, key, value):
#     dictionary[key] = value
#     return dictionary

# # Создаем функцию удаления контакта
# def delete_contact(dictionary, key):
#     del dictionary[key]
#     return dictionary

# # Создаем функцию поиска ключа в словаре
# def key_check(dictionary, key):
#     try:
#         value = dictionary[key]
#         return f'Контакт {key} существует, значение: {value}'
#     except KeyError:
#         return f'Контакт {key} не найден'

# # Создаем функцию поиска значения в словаре
# def find_by_value(dictionary, value):
#     for key, val in dictionary.items():
#         if val == value:
#             return key
#     return f'Номер не найден...'

# # Создаем функцию отображения телефонной книги
# def show_phonebook(dictionary):
#     result = ['Список контактов:']

#     for key in sorted(dictionary):
#         result.append(f'  - {key}: {dictionary[key]}')

#     return '\n'.join(result)

# # Выводим результаты
# result_download_contact = download_contact(phonebook, "Смирнов", "456-78-90")
# print(result_download_contact)

# result_to_change_phone = to_change_phone(phonebook, "Петров", "999-99-99")
# print(result_to_change_phone)

# result_delete_contact = delete_contact(phonebook, "Сидорова")
# print(result_delete_contact)

# result_key_check = key_check(phonebook, "Иванов")
# print(result_key_check)

# result_show_phonebook = show_phonebook(phonebook)
# print(result_show_phonebook)

# result_find_by_value = find_by_value(phonebook, "234-56-78")
# print(result_find_by_value)

# *Кортежи (Tuples)*
# Задание: Координаты и расстояния
# Напишите программу для работы с координатами точек:
# Создайте кортеж  point_a  с координатами (3, 5)
# Создайте кортеж  point_b  с координатами (7, 2)
# Создайте кортеж  point_c  с координатами (1, 9)
# Выполните операции:
# Распакуйте координаты точки A в переменные x1, y1
# Найдите расстояние между точками A и B формула: √((x2-x1)² + (y2-
# y1)²)
# Найдите самую удаленную точку от начала координат (0,0)
# Создайте список  all_points , содержащий все три кортежа
# Попробуйте изменить координату точки A (объясните результат в комментарии)
# Для вычислений используйте  math.sqrt()
import math
point_a = (3, 5)
point_b = (7, 2)
point_c = (1, 9)

x1 = point_a[0]
y1 = point_a[1]

x2 = point_b[0]
y2 = point_b[1]

x3 = point_c[0]
y3 = point_c[1]

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f'Расстояние между точками A и B составляет: {distance}')

dist1 = math.sqrt(x1**2 + y1**2)
dist2 = math.sqrt(x2**2 + y2**2)
dist3 = math.sqrt(x3**2 + y3**2)

if dist1 > dist2 and dist1 > dist3:
    print('Самая удаленная - точка А')
elif dist2 > dist1 and dist2 > dist3:
    print('Самая удаленная - точка B')
else:
    print('Самая удаленная - точка C')

all_points = [
    point_a,
    point_b,
    point_c
]

print(all_points)

# all_points[0][0] = 5 # TypeError: 'tuple' object does not support item assignment
# Кортежи неизменяемы (immutable) — это их ключевое свойство, в отличие от списков.