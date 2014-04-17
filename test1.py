# -*- coding: utf-8 -*-
import logging, urllib
logging.basicConfig(level=logging.DEBUG)
from grab import Grab
g = Grab()


def gsearch (query,query_2):
    """ парсит результаты поисково выдачи гугла. выдает список результатов"""

    #гуглострока
    search_str = 'https://www.google.com/search?q='

    #собсно поисковый запрос
    g.go(search_str+urllib.quote(query))

    #собираем ссылки из выдачи
    query_obj = g.doc.select('//h3[@class="r"]//a/@href')

    #прогоняем полученный массив ссылок через массив и делаем с ним все что угодно
    step2(query_obj,query_2)
    #print pers_u
    #print g.doc.select('//title').text()
    #нужно искать ссылки в которые заканчиваются на .txt и брать сразу их html

def step2 (query_obj,query_2):
    """ обработка списка результатов выдачи гугла """

    #идем по ссылке
    for elem in query_obj:
        n = Grab()
        n.go(elem.text())

        #если ответ 200 берем все ссылки со страницы
        if n.response.code == 200:
            query_obj2 = n.doc.select('//a')

            for elem2 in query_obj2:

                #ищем с тексте ссылки нужный нам текст
                if elem2.text().find(query_2.decode("UTF-8")) != -1:
                    print '<a href='+elem2.select('//@href').text()+'>'+elem2.text()+'</a>'

gsearch('ремешки для часов цена','ремешки')