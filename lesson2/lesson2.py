from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint
import re
import pandas as pd
# https://www.kinopoisk.ru/popular/films/?quick_filters=serials&tab=all
##https://hh.ru/search/vacancy?area=&fromSearchLine=true&st=searchVacancy&text=python
job = input("Введите ваш запрос ")
main_link = 'https://hh.ru'
params = { 'fromSearchLine':'true',
          'st':'searchVacancy',
          'text': job}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 YaBrowser/21.2.2.101 Yowser/2.5 Safari/537.36'}

response = requests.get(main_link + '/search/vacancy?area=', params=params, headers=headers)
if response.ok:
    soup = bs(response.text, 'html.parser')
    vacancy_list = soup.findAll('div', {'class':'vacancy-serp-item'})
    # pprint(serials_list)
    serials = []
    for vacancy in vacancy_list:
        vacancy_data = {}
        vacancy_name = vacancy.find('a')
        vacancy_link = vacancy_name['href']
        vacancy_name = vacancy_name.getText()
        vacancy_salary = vacancy.find('span',{'data-qa':'vacancy-serp__vacancy-compensation'})
        if not vacancy_salary:
            vacancy_salary_min = None
            vacancy_salary_max = None
            vacancy_salary_currency = None
        else:
            vacancy_salary = vacancy_salary.getText() \
                .replace(u'\xa0', u'')

            vacancy_salary = re.split(r'\s|-', vacancy_salary)

            if vacancy_salary[0] == 'до':
                vacancy_salary_min = None
                vacancy_salary_max = int(vacancy_salary[1])
            elif vacancy_salary[0] == 'от':
                vacancy_salary_min = int(vacancy_salary[1])
                vacancy_salary_max = None

            else:
                vacancy_salary_min = int(vacancy_salary[0])
                vacancy_salary_max = int(vacancy_salary[1])

            vacancy_salary_currency = vacancy_salary[2]

        vacancy_data['salary_min'] = vacancy_salary_min
        vacancy_data['salary_max'] = vacancy_salary_max
        vacancy_data['salary_currency'] = vacancy_salary_currency

        vacancy_data['name'] = vacancy_name
        vacancy_data['link'] = vacancy_link
        vacancy_data['salary'] = vacancy_salary
        vacancy_data['site'] = 'hh.ru'

        serials.append(vacancy_data)
    df = pd.DataFrame(serials)

pprint(df)