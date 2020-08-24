from requests import get
from bs4 import BeautifulSoup


class Corona:
	def __init__(self):
		self.__countries = self.__get_countries()

	# private method to read in viable country requests
	@staticmethod
	def __get_countries():
		file = open("countries.txt", "r")
		countries = file.read()
		file.close()

		countries = countries.split("\n")

		return countries

	# to check against valid countries
	def valid_countries(self):
		countries = self.__get_countries()

		for country in countries:
			country = country.replace("/", "")

		return countries

api = Corona()


def get_cases_by_country(country, page):
    if country == "total":
    	return get_total_cases(get_page())
    else:
    	try:
    		return get_total_cases(page)
    	except IndexError:
    		return None


def get_deaths_by_country(country, page):
    try:
    	return get_total_deaths(page)
    except IndexError:
    	return None


def get_recoveries_by_country(country, page):
	try:
		return get_total_recoveries(page)
	except IndexError:
		return None


def get_page():
    return get("https://www.worldometers.info/coronavirus/").text


def get_page_by_country(country):
	return get(f"https://www.worldometers.info/coronavirus/country/{country.strip().lower()}").text


def get_total_cases(page):
	soup = BeautifulSoup(page, "html.parser")
	divs = soup.findAll("div", {"class": "maincounter-number"})

	span = divs[0].findAll("span")
	span = str(span[0].text)

	span = span.replace(",", "")

	try:
		return span.strip()
	except AttributeError:
		return span


def get_total_deaths(page):
	soup = BeautifulSoup(page, "html.parser")
	divs = soup.findAll("div", {"class": "maincounter-number"})

	span = divs[1].findAll("span")
	span = str(span[0].text)

	span = span.replace(",", "")

	try:
		return span.strip()
	except AttributeError:
		return span


def get_total_recoveries(page):
	soup = BeautifulSoup(page, "html.parser")
	divs = soup.findAll("div", {"class": "maincounter-number"})

	span = divs[2].findAll("span")
	span = str(span[0].text)

	span = span.replace(",", "")

	try:
		return span.strip()
	except AttributeError:
		return span


def check_valid(country="total"):
	if country == "total":
		if "/" + country + "/" in api.valid_countries():
			return True
		else:
			return False
	else:
		return True


def valid_countries():
	countries = api.valid_countries()
	for country in countries:
		print(country)


def total_data():
	page = get_page()
	return [int(get_total_cases(page)), int(get_total_deaths(page)), int(get_total_recoveries(page))]


def total_data_by_country(country):
	page = get_page_by_country(country)

	try:
		return [int(get_cases_by_country(country, page)), int(get_deaths_by_country(country, page)),int(get_recoveries_by_country(country, page))]
	except ValueError:
		return [get_cases_by_country(country, page), get_deaths_by_country(country, page), get_recoveries_by_country(country, page)]
	except AttributeError:
		return [get_cases_by_country(country, page), get_deaths_by_country(country, page), get_recoveries_by_country(country, page)]
