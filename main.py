import psycopg2

from src.db_manager import DBManager

"""Connect to db"""
conn = psycopg2.connect(
    host='localhost',
    database='job',
    user='postgres',
    password='o977kx'
)

"""Create cursor"""
cur = conn.cursor()

db_manager = DBManager()


def employers():
    for i in db_manager.get_companies():
        value = (
            int(i['id']),
            i['name']
        )
        cur.execute('INSERT INTO employers VALUES (%s, %s)', value)
        conn.commit()


def get_id_employer(company_name: str) -> int:
    cur.execute("SELECT employer_id FROM employers WHERE employer_name = %s", (company_name,))
    result = cur.fetchone()
    return result[0] if result else None


def vacancies():
    for i in db_manager.get_all_vacancies():
        values = (
            get_id_employer(i['company_name']),
            i['company_name'],
            i['job_title'],
            i['link'],
            i['salary'],
        )
        cur.execute('INSERT INTO vacancies (employer_id, employer_name, job_title, link, salary) VALUES (%s, %s, %s, %s, %s)', values)
        conn.commit()


# employers()
vacancies()
