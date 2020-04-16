from entities_solution import Film, Planet
import utilities_solution as utl

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
    response = utl.get_resource(f"{ENDPOINT}/films")
    swapi_films = response['results']

    # 1.1 For loop: create list of Film objects
    # films = []
    # for film in swapi_films:
    #     films.append(Film(
    #         film['url'],
    #         film['title'],
    #         film['episode_id'],
    #         film['release_date'],
    #         film['planets']
    #         )
    #     )

    # 1.2 List comprehension
    films = [
        Film(
            film['url'],
            film['title'],
            film['episode_id'],
            film['release_date'],
            film['planets']
        ) for film in swapi_films
    ]

    # 1.3 Film count
    print(f"\nFilm count = {len(films)}\n")

    # 1.4 Print Film names
    for film in films:
        print(film) # leverage def __str__(self))

    print("\n") # padding


    # 2.0 ROMAN NUMERALS
    # Write conversion function

    # 2.1 Add Roman numerals
    for film in films:
        film.episode_roman_num = utl.convert_to_roman_numeral(int(film.episode_id))

    # 2.2 print film names (right justify Roman Numeral)
    for film in films:
        roman_num = utl.format_roman_numeral(film.episode_roman_num, 3)
        print(f"Episode {roman_num}: {film.title}")

    print("\n") # padding

    # 3.0 LIMIT PLANET CALLS TO SWAPI

    # 3.1 Create a crude cache
    planet_cache = {}

    # 3.2 Acquire planet info

    # for film in films[:2]: # test with first two films in list
    for film in films:
        roman_num = utl.format_roman_numeral(film.episode_roman_num, 3)
        print(f"Episode {roman_num}: {film.title}\n")
        for i, url in enumerate(film.planets):

            # Seed dict
            if i == 0:
                response = utl.get_resource(url)
                planet_cache[url] = Planet(response['url'], response['name'], response['population'])

            # Check cache
            if url not in planet_cache.keys():
                response = utl.get_resource(url) # Get planet
                planet = Planet(response['url'], response['name'], response['population'])
                planet_cache[url] = planet
            else:
                planet = planet_cache[url]

            # Update film object
            film.planets[i] = planet

    # 3.3 Print cache size
    print(f"\nPlanet cache size (calls made) = {len(planet_cache)}\n")


    # 4.0 BONUS: SORT BY EPISODE ID

    # Use built-in sorted() and a lambda (anonymous) function
    # Tutorial: https://www.afternerd.com/blog/python-sort-list/
    # Format: sorted(<list>, key = lambda <object>: <expression>)

    episodes = sorted(films, key = lambda film: film.episode_id)
    # episodes = sorted(films, key = lambda film: film.episode_id, reverse=True)

    # Print (right justify Roman Numeral)
    for episode in episodes:
        roman_num = utl.format_roman_numeral(episode.episode_roman_num, 3)
        print(f"Episode {roman_num}: {episode.title}")


    # 5.0 WRITE TO FILE
    filepath = 'sw_films.json'
    utl.write_custom_json(filepath, films)


if __name__ == '__main__':
    main()