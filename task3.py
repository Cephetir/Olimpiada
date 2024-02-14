from csv import DictReader


def findByCompanyName():
    """
    Спрашивает у пользователя название компании и выводит все вакансии по запросу.
    """

    while True:
        company = input('Введите название компании: ')

        if company == "None":
            break  # Выход

        # Читаем файл
        file = DictReader(open('vacancy.csv', encoding='UTF-8'), delimiter=';')

        # Считываем вакансии в массив соответствующие компании
        vacancies = []
        for vacancy in file:
            if vacancy['Company'] == company:
                vacancies.append(vacancy)

        if len(vacancies) == 0:
            print('К сожалению, ничего не удалось найти')
        else:
            # Выводим вакансии на экран
            for vacancy in vacancies:
                print(f"В {vacancy['Company']} найдена вакансия: {vacancy['Role']}. З/п составит: {vacancy['\ufeffSalary']}")
