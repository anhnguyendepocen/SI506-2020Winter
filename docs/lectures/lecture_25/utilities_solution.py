import json
import requests


class CustomEncoder(json.JSONEncoder):
    """WARNING: DO NOT MODIFY.

    Extends the json module's JSONEncoder class in order to serialize
    composite class instances.

     Note: include the pylint disable comment as Windows users have
     reported issues when the default() method is called.

     Methods:
        default: overrides default method
     """

    def default(self, obj): # pylint: disable=E0202
        """Check object is provisioned with a jsonable method that is
        callable. If yes override default serialization handling.

        Parameters:
            obj (object): class instance

        Returns:
            dict: dictionary representation of the object
        """

        if hasattr(obj, 'jsonable') and callable(obj.jsonable):
            return obj.jsonable()
        else:
            return json.JSONEncoder.default(self, obj)


def convert_to_roman_numeral(value, reverse=False):
    """Return Equivalent Roman numeral equivalent of passed in Arabic numeral.

    Parameters:
        value (int): Arabic value to convert

    Returns:
        str: Roman numeral
    """

    # Tuples to the rescue
    roman = ((1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V'), (6, 'VI'), (7, 'VII'))

    if 1 <= value <= 7:
        return roman[value - 1][1]
    else:
        raise ValueError ('Argument value must be between 1 and 7')


def format_roman_numeral(roman_numeral, max_chars):
    """Use str.rjust(n, chars) to return a string of length n. If the original string
    length is < n, then pad with additional chars (default = space) in order to attain
    length n.

    Parameters:
        value (str): string to right justify
        max_length (int): max_length of longest string

    Returns:
        str: right justified string

    """

    chars = len(roman_numeral)

    if chars == max_chars:
        return roman_numeral # no padding
    elif chars < max_chars:
        return roman_numeral.rjust(chars + (max_chars - chars))
    else:
        raise ValueError ('max_chars value must be greater than len(roman_numeral).')


def get_resource(url, params=None, timeout=20):
    """TODO
    """

    if params:
        response = requests.get(url, params=params, timeout=timeout).json()
    else:
        response = requests.get(url, timeout=timeout).json()

    return response



def write_custom_json(filepath, obj):
    """Serializes complex objects (e.g., composite class instances) as JSON
    by adding a CustomEncoder to the json.dump() call. Writes content to the
    provided filepath.

    Parameters:
        filepath (str): the path to the file.
        data (dict): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf-8') as file_obj:
        json.dump(obj, file_obj, cls=CustomEncoder, ensure_ascii=False, indent=2)