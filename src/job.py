from abc import ABC, abstractmethod


class Job(ABC):

    @abstractmethod
    def all_vacancies(self):
        """Получение всех вакансий"""
        pass

    @abstractmethod
    def get_vacancies(self, title):
        """Получение вакансий по ключевому слову"""
        pass
