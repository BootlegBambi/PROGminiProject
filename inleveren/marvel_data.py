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
    """:return: the dictionary (only containing character-related info) from 1 random character"""
    total = get_numberofcharacters()
    offset = random.randint(0, (total -1))
    data = marvel_conn.get_data("/v1/public/characters", {'offset': offset, 'limit': '1'})
    chosen_char = data['data']['results'][0]
    return chosen_char


def get_character_ID(char_dict):
    """
    :param char_dict: dictionary only containing character-related info from character.
    :returns: ID of character
    """
    char_ID = char_dict['id']
    return char_ID


def get_image_url(char_dict):
    """
    :param char_dict: dictionary only containing character-related info from character.
    :return: URL to image/thumbnail portraying said character.
    """
    url = char_dict['thumbnail']['path']

    if 'image_not_available' in url:
        url = 'https://i.pinimg.com/originals/24/92/00/249200c431fe811110761709b303fcaf.jpg'
    else:
        url = url + '/portrait_fantastic.' + char_dict['thumbnail']['extension']

    return url


def get_character_name(char_dict):
    """
    :param char_dict: dictionary only containing character-related info from character.
    :return: name corresponding to said character.
    """
    name = char_dict['name']
    if '(' and ')' in name:
        start = '('
        end = ')'
        real_name = (name.split(start))[1].split(end)[0]
        name = name.replace('(' + real_name + ')', '')
    return name


def get_character_id(char_dict):
    id = char_dict['id']
    return id


def replace_charname(str, name):
    """Replaces the character name in the str and return the new string."""
    if name.strip() in str:
        str.replace(name.strip(), 'XXX ')
    return str


def get_character_description(char_dict, char_name=None):
    """
    :param char_dict: dictionary only containing character-related info from character.
    :param char_name: name of character. Only needed for chosen character, so defaults to None in case it is called for other characters.
    :return: description of said character.
    :return: False if description is empty
    """
    description = char_dict['description']
    if description == '':
        return False
    elif char_name == None:
        pass
    elif char_name.strip() in description:
        return description.replace(char_name.strip(), 'XXX ')
    else:
        return replace_charname(description, get_character_name(char_dict))

    
def get_comic_ID(char_dict):
    """
    :param char_dict: dictionary only containing character-related info from character.
    :return: ID of the comic the character is in.
    :return: False if there are no comic books.
    """
    data = marvel_conn.get_data(f"/v1/public/characters/{get_character_ID(char_dict)}/comics")
    total = data['data']['count']
    if total == 0:
        return False
    number = random.randint(0, (total - 1))
    random_comic = data['data']['results'][number]['id']
    return random_comic


def get_comic_name(char_dict):
    """
    :param char_dict: dictionary only containing character-related info from character.
    :return: name of a comic (same comic from get_comic_ID()) the character is in.
    :return: False if there are no comic books.
    """
    comic_ID = get_comic_ID(char_dict)

    if comic_ID == False:
        return False
    data = marvel_conn.get_data(f"/v1/public/comics/{comic_ID}")
    comic_name = data['data']['results'][0]['title']
    hint = f'This character appears in the comic {comic_name}'
    return replace_charname(hint, get_character_name(char_dict))


def get_serie(char_dict):
    """
    :param char_dict: dictionary only containing character-related info from character.
    :return: a series the character is in.
    :return: False if there are no series.
    """
    total = char_dict['series']['returned']
    if total == 0:
        return False
    number = random.randint(0, (total - 1))
    random_series = char_dict['series']['items'][number]['name']
    hint = f'This character appears in series {random_series}'
    return replace_charname(hint, get_character_name(char_dict))


def get_other_char_in_comic(char_dict):
    """
    :param char_dict: dictionary only containing character-related info from character.
    :return: a different random character of a comic book the character is in.
    :return: False if there are no comics.
    """
    comic_ID = get_comic_ID(char_dict)
    if comic_ID == False:
        return False
    data = marvel_conn.get_data(f'/v1/public/comics/{comic_ID}/characters')
    total = data['data']['count']
    if total == 0:
        return False
    number = random.randint(0, (total - 1))
    random_other_char = data['data']['results'][number]['name']
    hint = f'This character appears in a comic together with {random_other_char}'
    return replace_charname(hint, get_character_name(char_dict))

    
def dictionary_random_characters():
    """
    :return: Dictionary of 5 random characters (keys 1-5) with their respective name, image, and description(if available)
    Visual:
    {
    1: {
        id: '',
        name: '',
        image: '',
        description: ''
        }
    2: {
        ....
        }
    }
    """
    dict = {}
    for x in range(1, 6):
        char = choose_character()
        if get_character_description(char) == False:
            dict.update({x: {'id': get_character_id(char), 'chosen': False, 'name': get_character_name(char), 'image': get_image_url(char)}})
        else:
            dict.update({x: {'id': get_character_id(char), 'chosen': False, 'name': get_character_name(char), 'image': get_image_url(char), 'description': get_character_description(char)}})
    return dict


def char_in_same_story_as(character):
    """
    Returns a hint about the character passed as parameter
    :param character: Dictionary with charachter information
    :return string: Hint to help find the character.
    """
    story_url = character['stories']['collectionURI']
    story_url.replace('http://gateway.marvel.com', '')

    stories = marvel_conn.get_data(story_url)
    if len(stories['data']['results']) > 0:
        if stories['data']['results'][0]['characters']['returned'] > 0:
            max = stories['data']['results'][0]['characters']['returned']-1
            number = random.randint(0, max)
            random_char = stories['data']['results'][0]['characters']['items'][number]['name']
            return "This character appears in the same serie(s) as {}".format(random_char)
        else:
            return "No other main characters or groups appear in the same serie(s) as this character."
    else:
        return "No other main characters or groups appear in the same serie(s) as this character."


def create_character_list(characters_wrong, character_correct):
    """
    :param characters_wrong: List of character dictionaries
    :param character_correct: Dictionary with character data.
    :return: List with all character dictionaries, with the attribute chosen set to True for the correct character.
    """
    characters_all = []
    character_correct['chosen'] = True

    for char_key in characters_wrong:
        characters_all.append(characters_wrong[char_key])
    characters_all.append(character_correct)
    return characters_all


def shuffellist(characters_all):
    """Shuffles the character list"""
    random.shuffle(characters_all)


def insert_newlines(string, every=50):
    return '\n'.join(string[i:i+every] for i in range(0, len(string), every))


def format_hint(hint):
    hint = insert_newlines(hint)
    return hint
