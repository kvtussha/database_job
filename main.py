from pprint import pprint

from src.db_manager import DBManager

db_manager = DBManager()
data = db_manager.need_full_vacancies()


def user_interaction():
    companies = db_manager.get_companies()
    print(f'Список со словарями с информацией о компаниях: {companies}')

    vacancies_count = db_manager.get_vacancies_count()
    print(f'Словарь с названием компании и количеством ее вакансий: {vacancies_count}')

    all_vacancies = db_manager.get_all_vacancies()
    print(f'Список с важной информацией о вакансии: {all_vacancies}')

    avg_salary = db_manager.get_avg_salary()
    print(f'Средняя зарплата по вакансиям: {avg_salary}')

    vacancies_higher_salary = db_manager.get_vacancies_with_higher_salary()
    print(f'Список вакансий с зарплатой выше среднего: {vacancies_higher_salary}')

    vacancies_keyword = db_manager.get_vacancies_with_keyword('менеджер', data)
    print(f'Список вакансий по ключевому слову: {vacancies_keyword}')


if __name__ == "__main__":
    user_interaction()