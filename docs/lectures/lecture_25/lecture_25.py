from entities import Film, Planet
import utilities as utl

# Specification
#
# Utilize lecture_25.py to retrieve SWAPI Films (n=7). For each film filter on
# 'url', 'name', and 'planets' properties only.
#
# Create a Film class (composite) and a Planet class (component) to hold SWAPI
# data in a separate module (entities.py).
#
# For each Film object add an instance variable to hold the Roman numeral
# equivalent of the episode id. Add the Roman numeral to the film object based
# on the Arabic episode id (e.g., V = 5). When printing Roman numerals to screen
# right justify by Roman numeral max length (e.g., 'VII' = 3; pad 'I' with 2
# spaces).
#
# For each planet associated with a film, retrieve the SWAPI
# representation of the planet, filtering on 'url', 'name', and 'population'
# properties only.
#
# Individual planets may be associated with more than one film. Make one and
# only one GET request to retrieve data on each planet (i.e., avoid making
# multiple calls to retrieve data already acquired from SWAPI) in order to
# optimize performance of the script.
#
# Serialize/encode the film objects as JSON and write to a file named
# 'sw_films.json',
#
# Add any utility functions written to provided utilities module (utilities.py).
#
# BONUS: sort the films by episode id before writing to file.
#
# Film references to planets
#
# Episode 4 = 3 planets
# Episode 5 = 4 planets
# Episode 6 = 5 planets
# Episode 1 = 3 planets
# Episode 2 = 5 planets
# Episode 3 = 13 planets
# Episode 7 = 1 planets
# Potentially 34 calls to retrieve data (yikes!)


ENDPOINT = "https://swapi.py4e.com/api"


def main():
    """TODO"""

    # 1.0 GET SWAPI Films (n = 7)


    # 2.0 ROMAN NUMERALS


    # 3.0 LIMIT PLANET CALLS TO SWAPI


    # 4.0 BONUS: SORT BY EPISODE ID

    # Use built-in sorted() and a lambda (anonymous) function
    # Tutorial: https://www.afternerd.com/blog/python-sort-list/
    # Format: sorted(<list>, key = lambda <object>: <expression>)


    # 5.0 WRITE TO FILE
    filepath = 'sw_films.json'


if __name__ == '__main__':
    main()