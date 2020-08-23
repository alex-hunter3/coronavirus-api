# example program to get data
import corona

# main function to return list [cases, deaths, recovered]
print(str(corona.get_country_data()) + "\n")

# function returns valid country names that can be used in the program
print(str(corona.valid_countries()) + "\n")

# function takes in a string to check if the string passed in is a valid country name
print(str(corona.check_valid("us")) + "\n")