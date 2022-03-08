from ast import parse
import requests
from bs4 import BeautifulSoup


URL = 'https://www.select.by/kurs'


def ConvertToRub(dollars):
    q = requests.get(URL)
    content = q.content
    soup = BeautifulSoup(content, 'lxml')

    RubInDollars = soup.select_one(
        '''.kursy-osnovnyh-valyut-cb section table
        tbody tr:first-child td:nth-child(3)'''
    ).text.strip()
    return float(RubInDollars.replace(',', '.')) * dollars


print(ConvertToRub(7))
