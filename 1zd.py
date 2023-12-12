import csv

employees = [
    {'Имя': 'Густав', 'Зарплата': 25000, 'Должность': 'Стажер-битмейкер'},
    {'Имя': 'Максим', 'Зарплата': 100000, 'Должность': 'Продюсер'},
    {'Имя': 'Люся', 'Зарплата': 35000, 'Должность': 'Менеджер'}
]

file_name = 'employees.csv'

with open(file_name, 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['Имя', 'Зарплата', 'Должность']
    writer = csv.DictWriter(file, fieldnames)

    writer.writeheader()
    for employ in employees:
        writer.writerow(employ)