from csv import DictReader


def groupCompanies():
    """
    Группируем все вакансии по названию их компании

    :return: Хэш-таблица всех компаний
    """

    # Читаем файл
    file = DictReader(open('vacancy.csv', encoding='UTF-8'), delimiter=';')

    # Считываем вакансии и группируем по компании
    companies = {}
    for vacancy in file:
        company = vacancy['Company']
        if company in companies.keys():
            companies[company].append(vacancy)
        else:
            companies[company] = [vacancy]

    # Возвращаем таблицу
    return companies


def printTopCompany(companies):
    """
    Выводит на экран все вакансии от компании с наибольшим количеством вакансий.
    :param companies: Таблица компаний
    """

    # Сортируем компании по количеству вакансий и берем первую компанию
    topCompany = sorted(companies.keys(), reverse=True, key=lambda company: len(companies[company]))[0]

    # Выводим на экран все вакансии этой компании
    for vacancy in companies[topCompany]:
        print(vacancy['Role'], ',', vacancy['\ufeffSalary'], ',', vacancy['Work_Type'])
