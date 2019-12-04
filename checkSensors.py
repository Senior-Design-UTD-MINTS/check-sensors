from bs4 import BeautifulSoup
from selenium import webdriver
import os
import sys

# Update location with where you downloaded PhantomJS (https://phantomjs.org/download.html)
PHANTOMJS_PATH_ENV_VAR = "PHANTOMJS_INSTALL"


def get_phantomJS_path():
    executable_path = os.environ.get(PHANTOMJS_PATH_ENV_VAR)
    if executable_path is None:
        sys.exit("Error: System needs to have the environment variable {} set to where phantomJS is installed on your system".format(
            PHANTOMJS_PATH_ENV_VAR))
    else:
        return executable_path


def get_sensors(phantomjs_path):
    driver = webdriver.PhantomJS(phantomjs_path)
    driver.get('http://mintsdata.utdallas.edu:4200/files#/')

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    test = soup.find_all('div')

    fin = []

    for div in test:
        if div.table is not None:
            for tr in div.table.tbody:
                try:
                    fin.append(tr.td.input['value'])
                except:
                    pass

    return fin
