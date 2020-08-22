import flask

from bs4 import BeautifulSoup
from requests import get


def get_case_by_country(country="TOTAL"):
    pass


def get_page():
    return get("https://www.worldometers.info/coronavirus/").text


def get_total_cases():
	page = get_page()

	soup = BeautifulSoup(page, "html.parser")
	divs = soup.findAll("div", {"class": "maincounter-number"})

	span = divs[0].findAll("span")
	span = str(span[0])
	span = span.replace('<span style="color:#aaa">', "")
	span = span.replace(' </span>', '')

	return span
