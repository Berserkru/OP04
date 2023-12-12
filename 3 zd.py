import csv

file_name = 'employees.csv'

new_employees = [
    {'Имя': 'Ваcя', 'Зарплата': 10000, 'Должность': 'водитель-мусоровоза'},
    {'Имя': 'Ян', 'Зарплата': 40000, 'Должность': 'Ресторатор'}]

with open(file_name, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    for employ in new_employees:
        writer.writerow([employ['Имя'], employ['Зарплата'], employ['Должность']])
print(f'Данные успешно записаны в файл:{file_name}')