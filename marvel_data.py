import marvel_conn
import random

def get_numberofcharacters(data=marvel_conn.get_data("/v1/public/characters", {'limit': '1'})):
    """
    :param data: Optional. Insert a dataset return form the Marvel API.
    If no data is entered this function makes a call to the Marvel API and uses that data.
    :return: The number of total characters
    :return: False (0) if no correct data is supplied.
    """
    if data:
        try:
            numofcharacters = data['data']['total']
            return numofcharacters
        except NameError:
            return False
    return False


def choose_character():
    '''':return: the dictionary (only containing character-related info) from 1 random character'''
    total = get_numberofcharacters()
    offset = random.randint(0, (total -1))
    data = marvel_conn.get_data("/v1/public/characters", {'offset': offset, 'limit': '1'})
    chosen_char = data['data']['results']
    return chosen_char
