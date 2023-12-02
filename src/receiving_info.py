from settings.implemented import cur


class ReceivingInfo:
    """
    A class that receives data from the job database
    Methods:
        get_companies_and_vacancies_count:  gets the name of the company and the number of its vacancies
        get_all_vacancies: receives all vacancies of each employer
        get_avg_salary: receives an average salary for vacancies
        get_vacancies_with_higher_salary: gets jobs above the average salary
        get_vacancies_with_keyword: gets vacancies by keyword
    """

    @staticmethod
    def get_companies_and_vacancies_count() -> list:
        """
        Gets the name of the company and the number of its vacancies
        Return:
            list: a list with data
        """
        query = 'SELECT employer_name, count_vacancy FROM employers;'
        cur.execute(query)
        return cur.fetchall()

    @staticmethod
    def get_all_vacancies() -> list:
        """
        Receives all vacancies of each employer
        Return:
            list: a list with data
        """
        query = ('SELECT employer_name, job_title, vacancy_link, salary '
                 'FROM vacancies;')
        cur.execute(query)
        return cur.fetchall()

    @staticmethod
    def get_avg_salary() -> float:
        """
        Receives an average salary for vacancies
        Return:
            float: arithmetic mean of salaries
        """
        query = 'SELECT AVG(salary) FROM vacancies'
        cur.execute(query)
        return int(cur.fetchone()[0])

    @classmethod
    def get_vacancies_with_higher_salary(cls) -> list:
        """
        Gets jobs above the average salary
        Return:
            list: a list with data
        """
        query = f'SELECT * FROM vacancies WHERE salary > {cls.get_avg_salary()}'
        cur.execute(query)
        return cur.fetchall()

    @staticmethod
    def get_vacancies_with_keyword(word: str) -> list:
        """
        Gets vacancies by keyword
        Param:
            word: str, the keyword by which vacancies will be selected
        Return:
            list: a list with data
        """
        query = f"SELECT * FROM vacancies WHERE job_title LIKE '%{word}%'"
        cur.execute(query)
        return cur.fetchall()
