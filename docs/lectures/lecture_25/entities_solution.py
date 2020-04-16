class Film:
    """TODO"""

    def __init__(
        self,
        url,
        title,
        episode_id,
        release_date,
        planets
        ):

        self.url = url
        self.title = title
        self.episode_id = episode_id
        self.episode_roman_num = None
        self.release_date = release_date
        self.planets = planets

    def jsonable(self):
        """TODO"""

        return {
            "url": self.url,
            "title": self.title,
            "episode_id": self.episode_id,
            "episode_roman_numeral": self.episode_roman_num,
            "release_date": self.release_date,
            "planets": self.planets
        }

    def __str__(self):

        if self.episode_roman_num:
            return f"Episode {self.episode_roman_num}: {self.title}"
        else:
            return f"Episode {self.episode_id}: {self.title})"


class Planet:
    """TODO"""

    def __init__(self, url, name, population):
        self.url = url
        self.name = name
        self.population = population


    def jsonable(self):
        """TODO"""

        return {
            "url": self.url,
            "name": self.name,
            "populatioon": self.population
        }

    def __str__(self):

        return self.name
