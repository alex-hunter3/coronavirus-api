from flask import Flask
from bs4 import BeautifulSoup
from requests import get


app = Flask(__name__)


def get_cases_by_country(country="total"):
    if country == "total":
    	return get_total_cases(get_page())
    else:
    	page = get_page_by_country(country.lower())

    	try:
    		return get_total_cases(page)
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
	span = str(span[0])
	span = span.replace('<span style="color:#aaa">', "")
	span = span.replace(' </span>', '')

	return span


@app.route("/")
def total_cases():
	return f"{get_total_cases(get_page())}"


if __name__ == "__main__":
	app.run(debug=True)
	
