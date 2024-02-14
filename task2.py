from csv import DictReader


def quickSort(array):
    """
    Сортировать данный массив
    :param array: Сортируемый массив
    """

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key['Company_Size'] > array[j]['Company_Size']:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def printBestVacancies():
    """
    Выводит на экран вакансии с наименьшим количеством сотрудников на роль "классный руководитель".
    """

    # Читаем файл
    file = DictReader(open('vacancy.csv', encoding='UTF-8'), delimiter=';')

    # Считываем все вакансии в массив
    vacancies = []
    for vacancy in file:
        vacancies.append(vacancy)

    # Сортируем по количеству сотрудников
    quickSort(vacancies)

    # Выводим на экран вакансии классного руководителя
    for vacancy in vacancies:
        if vacancy['Role'] == "классный руководитель":
            print(f"В компании {vacancy['Company']} есть заданная профессия: {vacancy['Role']}, з/п в такой компании составит: {vacancy['\ufeffSalary']}")
