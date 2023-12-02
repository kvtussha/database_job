import json

import requests

from src.job import Job


class HeadHunterAPI(Job):
    """
    Class HeadHunterAPI is inherited from class Job. You can use this class
    to get information about vacancies in various formats.

    Attributes:
        _response_hh: return an object Response from address 'https://api.hh.ru/vacancies'
        to get information from the HeadHunter service.
        _response: return str with information about vacancies

    Methods:
        get_all_vacancies: converts the str information to json format and return the
        key we need (without setting keys) in dictionary.
        vacancies_by_profession: get vacancies by the name of the specialty
    """

    def __init__(self):
        self._response_hh = requests.get('https://api.hh.ru/vacancies')
        self._response = self._response_hh.text

    def get_all_vacancies(self) -> list:
        """
        Get all the vacancies, with full information about each one.
        Return:
             list: a list containing dictionaries with information about
             for each vacancy.
        """
        return json.loads(self._response)['items']

    def vacancies_by_profession(self, title: str) -> list | str:
        """
        Get vacancies by the name of the specialty.
        Param:
            title: str, the name of the specialty from the user
        Return:
            list: if there are vacancies with this specialty name, you will receive them
            str: if there are no vacancies with this specialty name, you will receive
            a phrase with an apology
        """
        vacancies = self.get_all_vacancies()
        need_results = [item for item in vacancies if title.lower() in item['name'].lower()]
        if need_results:
            return need_results
        else:
            return "No results found"
