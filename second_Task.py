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
#url для проверки http://pastebin.com/raw/2mie4QYa


import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

url = input()
def webLinks(url):
    urls = set()
    url_parsed = urlparse(url)
    link = url_parsed.netloc
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    #print(soup)
    #print(soup)
    for a_tag in soup.findAll('a'):
        href = a_tag.attrs.get('href') # Как я понял получает доступ напрямую к атрибуту href
        if href == '' or href is None:
            continue
        #href = urljoin(url, href)
    #print (href)

        parsed_href = urlparse(href)
        href = parsed_href.netloc


    #print(href)
        if href not in urls:
            urls.add(href)
    urls = list(urls)
    urls = sorted(urls)
    for i in urls:
        if ':' in i:
            i = i[:i.index(':')]
        print(i)

webLinks(url)
