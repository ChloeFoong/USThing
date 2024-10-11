import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse

def dynamic_endpoint(request,subject):
    url = f"https://w5.ab.ust.hk/wcq/cgi-bin/2410/subject/{subject}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    info_element = soup.find_all(class_='course')

    return HttpResponse(info_element)


