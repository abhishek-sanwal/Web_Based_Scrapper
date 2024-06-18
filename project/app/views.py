from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.http import HttpRequest, HttpResponse
from typing import List
from bs4 import BeautifulSoup
import requests


def getlink(request: HttpRequest) -> HttpResponse:
    '''

    This function represents a get and post view
    First this view will take url as input as get request
    than it will list all urls and name in same webpage.s

    '''
    form = request.POST or None

    if form.is_valid():

        url = form.cleansed_fields("url")
        messages.success(f"Your url has been received.{url}")
        form.save()
        links = extract_links(url)
        return render(request, template_name="Urls.html", context={
            "links": links
        })

    return render(request, template_name="Urls.html", context={
        "form": form
    })


def extract_links(url: str) -> List[List[str]]:
    '''

    This function uses beautifulSoup and requests module to extarct
    information form an html webpage through webscrapping.
    This function extracts all links inside body tag in given html page.
    '''
    # Fetch page
    res = requests.get(url)

    # Parse the webpage using a parser
    soup = BeautifulSoup(res.text, 'html.parser')

    print(soup.prettify())
    ret = list()
    # Find all links inside body tag
    for link in soup.find('body').find_all('a'):

        # Find value of href attribute inside anchor tags
        val = link.get('href')
        # Add val and val.text to list
        ret.append([val, link.text.strip()])

    return ret
