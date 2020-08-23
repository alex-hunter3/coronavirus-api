from requests import get
from bs4 import BeautifulSoup


def get_page():
	return get("https://www.worldometers.info/coronavirus/").text


def get_tags(page):
	countries = []
	soup = BeautifulSoup(page, "html.parser")
	countries_ = soup.find_all("a", {"class": "mt_a"}, href=True)

	for country in countries_:
		countries.append(country["href"])

	return countries


def write_file(countries):
	file = open("countries.txt", "w")

	for country in countries:
		print("/" + str(country)[8:])
		file.write("/" + str(country)[8:] + "\n")

	file.close()


write_file(get_tags(get_page()))