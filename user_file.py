from src.receiving_info import ReceivingInfo

info = ReceivingInfo()


def user_interaction():
    """
    A method for interacting with the user
    Return:
        None: because it just runs previously created methods in the class ReceivingInfo
    """
    print(f"Названия компаний и число их вакансий: {info.get_companies_and_vacancies_count()}")
    print(f"Получение всех вакансий выбранных работодателей: {info.get_companies_and_vacancies_count()}")
    print(f"Средняя зарплата: {info.get_avg_salary()}")
    print(f"Вакансии с зарплатой выше средней: {info.get_vacancies_with_higher_salary()}")
    print(f"Вакансии по ключевому слову: {info.get_vacancies_with_keyword('Python')}")


if __name__ == "__main__":
    user_interaction()
