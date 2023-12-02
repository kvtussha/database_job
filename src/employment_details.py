from pprint import pprint

import requests

from settings.implemented import hh_api, COMPANY_NAMES
from src.convert_salary import SalaryConversion


class EmploymentDetails:
    """
    A class for getting information about vacancies.
    The database will be filled with this information in the future

    Methods:
        employer_info: goes through the entire list of vacancies and searches
            for those whose name matches the established names in implemented.py
        complete_employer_info: prepares values about the employer for writing to the database
        vacancies_info: collects the most necessary information about each vacancy of each employer
    """

    @staticmethod
    def _employer_info() -> list | str:
        """
        Returns information about the employer.
        Return:
            list: if the name of the employer's company is found
            in the established company names (at least one)
            str: if no results are found
        """
        all_vacancies = hh_api.get_all_vacancies()
        employers = [item['employer'] for item in all_vacancies if item['employer']['name'] in COMPANY_NAMES]
        if employers:
            return employers
        else:
            return "Unfortunately, no employers were found from the established list"

    @classmethod
    def complete_employer_info(cls) -> list | str:
        """
        Counts the number of vacancies for each employer
        Returns:
            list: if you have managed to read the vacancies of employers, a list is returned
            with each employer and the number of his vacancies and his index
            str: otherwise, the line will contain an error in type str
        """
        info = cls._employer_info()
        company_jobs = []

        if isinstance(info, list) is True:
            for i in info:
                company_vacs = requests.get(i['vacancies_url']).json()['items']
                number_of_vacancies = len(company_vacs)
                new_employer = (i["id"], i["name"], number_of_vacancies)
                if new_employer not in company_jobs:
                    company_jobs.append(new_employer)
            return company_jobs
        else:
            return "An error occurred when receiving a list with information about the employer"

    @classmethod
    def vacancies_info(cls):
        """
        Creates a list of tuples with the most relevant information about the job
        Return:
            list: if all information about the job is collected
            str: if an error occurred and the data was not transmitted
        """
        info = cls._employer_info()
        salary_conv = SalaryConversion()
        result = []
        if isinstance(info, list) is True:
            for i in info:
                company_vacs = requests.get(i['vacancies_url']).json()["items"]
                for j in company_vacs:
                    salary = salary_conv.salary_value(j['salary'])
                    requirement = j['snippet']['requirement']
                    responsibility = j['snippet']['responsibility']
                    employer_id = int(j['employer']['id'])
                    vacancy = (employer_id, j['employer']['name'], j['name'], j['alternate_url'],
                               salary, requirement, responsibility)
                    result.append(vacancy)
            return result
        else:
            return "Sorry, information about employers has not been received"
