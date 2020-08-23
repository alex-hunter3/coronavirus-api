from requests import get


class Corona:
	def __init__(self):
		self.__countries = self.__get_countries()

		# to be changed to webserver ip, for the now will only work on local machine with api.py running
		self.__base_url  = "http://127.0.0.1:5000"

	# private method to read in viable country requests
	@staticmethod
	def __get_countries():
		file = open("countries.txt", "r")
		countries = file.read()
		file.close()

		countries = countries.split("\n")

		for country in range(len(countries)):
			countries[country] = countries[country]

		return countries

	# to check against valid countries
	def valid_countries(self):
		countries = self.__get_countries()

		for country in countries:
			country = country.replace("/", "")

		return countries

	def get_url(self):
		return self.__base_url


api = Corona()


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


# only function that needs to be used to collect data on any country on the worldometer website
def get_country_data(country="/"):
	country = country.replace("/", "").lower()

	check = check_valid(country)

	if not check:
		raise AttributeError("INVALID COUNTRY NAME. To check if country is valid use function check_valid(country_to_check). To get list of valid countries use valid_countries() function.")

	url = api.get_url() + "/" + country
	return (get(url).text).split(",")
