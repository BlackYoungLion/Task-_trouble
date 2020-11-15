from bs4 import BeautifulSoup
import  re
import requests
from urllib import parse

#pattern = r'<a.+href=[\'"]([^./][^\'"]*)[\'"]'
a = input().strip()
#
#List = re.findall(pattern, str(res.text))
#print(List)
#page = BeautifulSoup(str(res.content),'html.parser')
#print(page.prettify())

def webLinks(a):
    urls = set()
    domain_name = parse(a).netloc # по логике здесь я должен был вытаскивать имена доменов....но я не понимаю почему netloc не работает
    #res = requests.get(a)
    #page = BeautifulSoup(str(res.content), 'html.parser')4
    soup = BeautifulSoup(requests.get(a).content, 'html.parser')
    print(domain_name)

webLinks(a)
