from flask import Flask
from bs4 import BeautifulSoup
from requests import get


app = Flask(__name__)


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


@app.route("/")
def total_data():
	page = get_page()
	return f"{get_total_cases(page)},{get_total_deaths(page)},{get_total_recoveries(page)}"


@app.route("/<country>")
def total_data_by_country(country):
	page = get_page_by_country(country)
	return f"{get_cases_by_country(country, page)},{get_deaths_by_country(country, page)},{get_recoveries_by_country(country, page)}"


if __name__ == "__main__":
	app.run(debug=True)
	
