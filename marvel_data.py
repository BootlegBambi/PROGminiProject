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
    ''':return: the dictionary (only containing character-related info) from 1 random character'''
    total = get_numberofcharacters()
    offset = random.randint(0, (total -1))
    data = marvel_conn.get_data("/v1/public/characters", {'offset': offset, 'limit': '1'})
    chosen_char = data['data']['results']
    return chosen_char


def get_image_url(char_dict):
    '''
    :param char_dict: dictionary only containing character-related info from character.
    :return: URL to image/thumbnail portraying said character.
    '''
    url = char_dict[0]['thumbnail']['path']

    if 'image_not_available' in url:
        url = 'marvel_logo.jpg'
    else:
        url = url + '/portrait_fantastic.' + char_dict[0]['thumbnail']['extension']

    return url


def get_character_name(char_dict):
    '''
    :param char_dict: dictionary only containing character-related info from character.
    :return: name corresponding to said character.
    '''
    name = char_dict[0]['name']
    if '(' and ')' in name:
        start = '('
        end = ')'
        real_name = (name.split(start))[1].split(end)[0]
        name = name.replace('(' + real_name + ')', '')
    return name


def get_character_description(char_dict, char_name=None):
    ''''
    :param char_dict: dictionary only containing character-related info from character.
    :param char_name: name of character. Only needed for chosen character, so defaults to None in case it is called for other characters.
    :return: description of said character.
    :return: False if description is empty
    '''
    description = char_dict[0]['description']
    if description == '':
        return False
    elif char_name == None:
        pass
    elif char_name in description:
        return description.replace(char_name, 'XXX ')
    else:
        return description

    
def get_comic(char_dict):
    '''
    :param char_dict: dictionary only containing character-related info from character.
    :return: comic the character is in.
    :return: False if there are no comic books.
    '''
    total = char_dict[0]['comics']['available']
    if total == 0:
        return False
    number = random.randint(0, (total-1))
    random_comic = char_dict[0]['comics']['items'][number]['name']
    return random_comic    


def get_serie(char_dict):
    '''
    :param char_dict: dictionary only containing character-related info from character.
    :return: a series the character is in.
    :return: False if there are no series.
    '''
    total = char_dict[0]['series']['available']
    if total == 0:
        return False
    number = random.randint(0, (total - 1))
    random_series = char_dict[0]['series']['items'][number]['name']
    return random_series
    

def dictionary_random_characters(): #voor de random 9 keuze opties?
    ''''
    :return: Dictionary of 9 random characters (keys 1-9) with their respective name, image, and description(if available)
    Visual:
    {
    1: {
        name: '',
        image: '',
        description: ''
        }
    2: {
        ....
        }
    }
    '''
    dict = {}
    for x in range(1,9):
        char = choose_character()
        if get_character_description(char) == False:
            dict.update({x: {'name': get_character_name(char), 'image': get_image_url(char)}})
        else:
            dict.update({x: {'name': get_character_name(char), 'image': get_image_url(char), 'description': get_character_description(char)}})
    return dict

