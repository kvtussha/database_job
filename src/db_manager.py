from pprint import pprint

from src.hh import HeadHunterAPI


class DBManager:
    hh_api = HeadHunterAPI()

    @classmethod
    def get_companies(cls) -> list:
        """Возвращает информацию о работодателе"""
        company_names = []
        companies = []
        for i in cls.hh_api.all_vacancies():
            employer_name = i['employer']['name']
            if employer_name not in company_names and len(companies) < 10:
                companies.append(i['employer'])
                company_names.append(i['employer']['name'])
        return companies

    @classmethod
    def get_vacancies_count(cls) -> dict:
        """Возвращает словарь с компаниями и количеством вакансий у определенной компании"""
        vac_count_dict = {}
        for i in cls.hh_api.all_vacancies():
            for j in DBManager.get_companies():
                employer_name = i['employer']['name']
                if employer_name == j['name']:
                    if employer_name in vac_count_dict.keys():
                        vac_count_dict[employer_name] += 1
                    else:
                        vac_count_dict[employer_name] = 1
        return vac_count_dict

    @classmethod
    def get_all_vacancies(cls):
        """Возвращает самую нужную информацию у вакансии"""
        vacancies = []
        for i in cls.hh_api.all_vacancies():
            for j in DBManager.get_companies():
                employer_name = i['employer']['name']
                vac = {}
                if employer_name == j['name']:
                    vac['company_name'] = i['employer']['name']
                    vac['job_title'] = i['name']
                    vac['link'] = i['alternate_url']
                    vac['salary'] = cls._define_salary(i['salary'])
                    vacancies.append(vac)
        return vacancies

    @staticmethod
    def _define_salary(dct: dict):
        """Функция получает значение зарплаты"""
        if dct is None:
            return 0
        elif dct['from'] is not None:
            return dct['from']
        elif dct['to'] is not None:
            return dct['to']
        else:
            return 0

    @classmethod
    def get_avg_salary(cls):
        """Среднее по всем зарплатам"""
        vacancies = cls.get_all_vacancies()
        salaries = []
        for i in vacancies:
            salaries.append(i['salary'])
        result = round(sum(salaries) / len(salaries))
        return result

    @classmethod
    def get_vacancies_with_higher_salary(cls):
        """Вакансии с зарплатой выше средней"""
        vacancies = cls.get_all_vacancies()
        best_salary_vac = []
        for i in vacancies:
            if i['salary'] >= cls.get_avg_salary():
                best_salary_vac.append(i)
        return best_salary_vac

    @classmethod
    def need_full_vacancies(cls):
        full_vacancies = []
        for i in cls.hh_api.all_vacancies():
            for j in DBManager.get_companies():
                employer_name = i['employer']['name']
                if employer_name == j['name']:
                    full_vacancies.append(i)
        return full_vacancies

    @classmethod
    def get_vacancies_with_keyword(cls, word: str, data) -> list | str:
        result = []

        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, str) and word.lower() in value.lower():
                    result.append(data)
                else:
                    result.extend(cls.get_vacancies_with_keyword(word, value))
        elif isinstance(data, list):
            for item in data:
                result.extend(cls.get_vacancies_with_keyword(word, item))
        return result
        # if result:
        #     return result
        # else:
        #     return 'По такому ключевому слову вакансий не найдено'


db_manager = DBManager()
data = db_manager.need_full_vacancies()
# print(db_manager.get_vacancies_with_keyword('менеджер', data))
# pprint(db_manager.need_full_vacancies())
