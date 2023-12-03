import psycopg2
from dotenv import load_dotenv

from src.hh import HeadHunterAPI

import os

load_dotenv()

YOUR_ACCESS_KEY = os.getenv("API_KEY")
hh_api = HeadHunterAPI()
COMPANY_NAMES = ['Яндекс Команда для бизнеса', 'Пятёрочка', 'Aurum Queen', 'Бочкаревский пивоваренный завод',
                 'Легион', 'ЭМФИ', 'LiteJob', 'Точка', 'Белов Максим Германович',
                 'Посольство Малайзии в Республике Казахстан']
conn = psycopg2.connect(
    host="localhost",
    database="job",
    user="postgres",
    password=os.getenv("PASSWORD_DB")
)

cur = conn.cursor()
