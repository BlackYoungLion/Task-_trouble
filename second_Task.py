"""
Вашей программе на вход подается ссылка на HTML файл. Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов, которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида ﻿.

Сайты следует выводить в алфавитном порядке.

Пример HTML файла:

<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">
Пример ответа:

mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru
"""



from bs4 import BeautifulSoup
import  re
import requests
from urllib import parse

#pattern = r'<a.+href=[\'"]([^./][^\'"]*)[\'"]'
url = input()
#
#List = re.findall(pattern, str(res.text))
#print(List)
#page = BeautifulSoup(str(res.content),'html.parser')
#print(page.prettify())

def webLinks(url):
    urls = set()
    url_parsed = parse(url)
    link = url_parsed.netloc
    #res = requests.get(a)
    #page = BeautifulSoup(str(res.content), 'html.parser')4
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    print(link)

webLinks(url)
