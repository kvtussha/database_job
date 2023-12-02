from abc import ABC, abstractmethod


class Job(ABC):
    """
    The abstract class for platforms with employers and employees

    Methods:
        get_all_vacancies: retrieves information from the service and returns it in json format
        vacancies_by_profession: searches through the list of professions for vacancies
        with the specified name and returns them
    """

    @abstractmethod
    def get_all_vacancies(self) -> list:
        """
        Get all vacancies with full information
        Return:
            list with vacancies
        """
        pass

    @abstractmethod
    def vacancies_by_profession(self, title: str) -> list | str:
        """
        Get vacancies by name of speciality from user
        Attribute:
            title: name of specialize from user
        Return:
            list: if there are vacancies with this specialty name, you will receive them
            str: if there are no vacancies with this specialty name, you will receive
            a phrase with an apology
        """
        pass
