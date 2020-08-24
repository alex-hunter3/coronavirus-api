# example program to get data
import corona

# main function to return list [cases, deaths, recovered] of world data
print(corona.total_data())

# function to return country specific data
# returns all items as strings if there is an "N/A" in the list otherwise will be int list
print(corona.total_data_by_country("uk"))

# function returns valid country names that can be used in the program
print(str(corona.valid_countries()) + "\n")

# function takes in a string to check if the string passed in is a valid country name
print(str(corona.check_valid("uk")) + "\n")
