from csv import DictReader, DictWriter


def copy(fileName: str):
    """
    Копирует столбцы: Company, Role, Salary из таблицы в новый файл
    :param fileName: Название нового файла
    """

    # Читаем исходный файл
    file = DictReader(open('vacancy.csv', encoding='UTF-8'), delimiter=';')
    # Записываем в новый файл
    file2 = DictWriter(open(fileName, 'w', encoding='UTF-8', newline=''), ['company', 'role', 'Salary'])

    file2.writeheader()  # Печатаем заголовок
    # Печатаем все вакансии
    for vacancy in file:
        file2.writerow({'company': vacancy['Company'], 'role': vacancy['Role'], 'Salary': vacancy['\ufeffSalary']})


def print_top_salary():
    """
    Выводит на экран топ 3 самых высокооплачиваемых профессий в формате:
        <компания> - <вакансия> - <зарплата>
    """

    # Читаем исходный файл
    file = DictReader(open('vacancy_new.csv', encoding='UTF-8'))

    # Считываем все вакансии в массив
    vacancies = []
    for vacancy in file:
        vacancies.append(vacancy)

    # Сортируем по ЗП
    vacancies.sort(key=lambda vacancy: vacancy['Salary'], reverse=True)

    # Выводим на экран
    for vacancy in vacancies[:3]:
        print(vacancy['company'], '-', vacancy['role'], '-', vacancy['Salary'])
