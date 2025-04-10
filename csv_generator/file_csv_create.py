# from faker import Faker
# import random
#
# # Инициализируем Faker и иткрываем файл
# fake = Faker()
# with open('persons.csv', 'w') as file:
#     # Записываем заголовок
#     file.write("last_name;first_name;id\n")
#     # Генерируем 9999 записей
#     for id in range(1, 10000):
#         # Генерируем има и фамилию нужной длинны
#         first_name = fake.first_name()[:random.randint(4, 10)]
#         last_name = fake.last_name()[:random.randint(4, 10)]
#         # Форматируем ID с ведущими нулями
#         formatted_id = f"{id:04d}"
#         # Записываем в файл
#         file.write(f"{last_name};{first_name};{formatted_id}\n")
#
# print("File persons.csv was successfully created")

from faker import Faker
import random

fake = Faker()
with open("persons.csv", "w") as file:
    file.write("last_name;first_name;id\n")
    for id in range(1, 100):
        last_name = fake.last_name()[:random.randint(4, 10)]
        first_name = fake.first_name()[:random.randint(4, 10)]
        formatted_id = f"{id:04d}"
        file.write(f"{last_name};{first_name};{formatted_id}\n")
print("Successfully created person.csv file!")

