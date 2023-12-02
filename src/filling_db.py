from settings.implemented import cur, conn
from src.employment_details import EmploymentDetails

emp_details = EmploymentDetails()


class FillingDB:
    """
    A class for filling the database with information.
    Methods:
        employers: gets information from the method of the VacanciesInfo() class,
         and, if it is a list, fills in the database
        vacancies: gets information from the method of the VacanciesInfo() class,
         and, if it is a list, fills in the database
    """
    @staticmethod
    def employers() -> None | str:
        """
        Fills in the employees table in the job database
        Returns:
             None: if the database table is full and there are no errors
             str: if an error occurs and the result is not received
        """
        employer_info = emp_details.complete_employer_info()
        if isinstance(employer_info, list):
            for i in employer_info:
                cur.execute('INSERT INTO employers VALUES (%s, %s, %s)', i)
                conn.commit()
        else:
            return "Unfortunately, no employers were found from the established list"

    @staticmethod
    def vacancies():
        """
        Fills in the vacancies table in the job database
        Returns:
             None: if the database table is full and there are no errors
             str: if an error occurs and the result is not received
        """
        vacancies_info = emp_details.vacancies_info()
        if isinstance(vacancies_info, list):
            for i in vacancies_info:
                cur.execute('INSERT INTO vacancies (employer_id, employer_name, job_title, vacancy_link, salary, '
                            'requirement, responsibility) VALUES (%s, %s, %s, %s, %s, %s, %s)', i)
                conn.commit()
        else:
            return "Unfortunately, no vacancies were found"
