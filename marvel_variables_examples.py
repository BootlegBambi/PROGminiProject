import marvel_data as mvd

#  Select one correct character
character_correct = mvd.choose_character()
character_correct = character_correct[0]  # Reformat format of the correct_character

# Select random wrong character, and merge correct and wrong characters
characters_wrong = mvd.dictionary_random_characters()
characters_all = mvd.create_character_list(characters_wrong, character_correct)
# Shuffel character data list
mvd.shuffellist(characters_all)

#  hints players can ask for
#hint_comic = f'Dit character komt voor in de comic {mvd.get_comic(chosen_dict)}'

# 'In same serie as X' hint
#print(mvd.char_in_same_story_as(chosen_dict))





