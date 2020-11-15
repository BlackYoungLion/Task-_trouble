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
