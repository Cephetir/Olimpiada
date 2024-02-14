from csv import DictReader, DictWriter


def calculatePercent():
    """
    Вычисляет среднюю ЗП по типу трудоустройства, вычисляет процент от данной ЗП и сохраняет таблицу в новый файл "vacancy_procent.csv"
    :param salary: Данная заработная плата
    """

    # Читаем исходный файл
    file = DictReader(open('vacancy.csv', encoding='UTF-8'), delimiter=';')

    # Считываем все вакансии в массив
    vacancies = []
    for vacancy in file:
        vacancies.append(vacancy)

    # Сохраняем ЗП
    salaries = {}
    for vacancy in vacancies:
        workType = vacancy['Work_Type'].lower()
        if workType in salaries.keys():
            salaries[workType].append(int(vacancy['\ufeffSalary']))
        else:
            salaries[workType] = [int(vacancy['\ufeffSalary'])]

    # Вычисляем среднюю ЗП
    sr_salaries = {}
    for workType in salaries.keys():
        sr_salaries[workType] = sum(salaries[workType]) / len(salaries[workType])

    # Записываем в новый файл
    file2 = DictWriter(
        open('vacancy_procent.csv', 'w', encoding='UTF-8', newline=''),
        ['Salary', 'Work_Type', 'Company_Size', 'Role', 'Company', 'Percent']
    )

    file2.writeheader()  # Печатаем заголовок
    # Вычислюем процент и печатаем все вакансии
    for vacancy in vacancies:
        salary = int(vacancy['\ufeffSalary'])
        sr_salary = sr_salaries[vacancy['Work_Type']]
        percent = int(salary / sr_salary * 100)

        file2.writerow({
            'Salary': vacancy['\ufeffSalary'],
            'Work_Type': vacancy['Work_Type'],
            'Company_Size': vacancy['Company_Size'],
            'Role': vacancy['Role'],
            'Company': vacancy['Company'],
            'Percent': str(percent) + '%'
        })
