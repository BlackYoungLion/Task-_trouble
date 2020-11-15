"""
Рассмотрим два HTML-документа A и B.

Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега. Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B. Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

Sample Input 1:

https://stepic.org/media/attachments/lesson/24472/sample0.html

https://stepic.org/media/attachments/lesson/24472/sample2.html

Sample Output 1:

Yes

Sample Input 2:

https://stepic.org/media/attachments/lesson/24472/sample0.html

https://stepic.org/media/attachments/lesson/24472/sample1.html

Sample Output 2:

No

Sample Input 3:

https://stepic.org/media/attachments/lesson/24472/sample1.html

https://stepic.org/media/attachments/lesson/24472/sample2.html

Sample Output 3:

Yes

"""


import re
import requests

a = input()
b = input()
pattern = r'<a.*href="([^"]*)"'

def link_list(a): # функция которая создает лист ссылок согласно патерну
    res = requests.get(a)
    if res.status_code == 200:
        List = re.findall(pattern, str(res.content))
        if List !=[] or List != None: #проверка на то что лист не пустой
            #print(List)
            return List
        else:
            return print('No')

def Step_and_check(): # функция которя шагает по ссылкам и ищет соответсвие заданной в b
    List = link_list(a)
    for i in List:
        link_req = requests.get(i)
        #print(link_req.content)
        if b in str(link_req.content):
            print('Yes')
            break
        else:
            print('No')
            break



link_list(a)
Step_and_check()
