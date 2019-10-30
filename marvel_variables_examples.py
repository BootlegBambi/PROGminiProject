import marvel_data as mvd

#  variables all involving the chosen character AKA the correct answer this round
chosen_dict = mvd.choose_character()

chosen_name = mvd.get_character_name(chosen_dict)
chosen_image = mvd.get_image_url(chosen_dict)
chosen_description = mvd.get_character_description(chosen_dict)

#  contains all the randomly chosen characters; see marvel_data for structure dictionary
random_char_dict = mvd.dictionary_random_characters()

#  hints players can ask for
hint_comic = f'Dit character komt voor in de comic {mvd.get_comic(chosen_dict)}'
