import marvel_conn


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

