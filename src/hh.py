import json
from pprint import pprint

import requests

from src.job import Job


class HeadHunterAPI(Job):
    def __init__(self):
        self._response_hh = requests.get('https://api.hh.ru/vacancies')
        self._response = self._response_hh.text

    def all_vacancies(self):
        """Получение всей информации о вакансиях"""
        return json.loads(self._response)['items']

    def get_vacancies(self, title):
        """Получение информации о вакансии по названию специальности"""
        vacancies = self.all_vacancies()
        need_results = []
        for item in vacancies:
            if title.lower() in item['name'].lower():
                need_results.append(item)

        if need_results:
            return need_results
        else:
            return "Результатов не найдено"


# hh_api = HeadHunterAPI()
# pprint(hh_api.all_vacancies())


# hh_api = HeadHunterAPI()
# print(hh_api.get_vacancies("Водитель"))
