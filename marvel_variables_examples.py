import marvel_data as mvd

#  Select one correct character
character_correct = mvd.choose_character()
character_correct = character_correct[0]  # Reformat format of the correct_character

# Select random wrong character, and merge correct and wrong characters
characters_wrong = mvd.dictionary_random_characters()
characters_all = mvd.create_character_list(characters_wrong, character_correct)
# Shuffel character data list
mvd.shuffellist(characters_all)

#  hints players can ask for (returns False if not available)
hint_serie = mvd.get_serie(character_correct)
hint_comic = mvd.get_comic_name(character_correct)
hint_description = mvd.get_character_description(character_correct, mvd.get_character_name(character_correct))

# 'In same serie as X' hint
#print(mvd.char_in_same_story_as(chosen_dict))
hint_other_char_in_comic = mvd.get_other_char_in_comic(chosen_dict)





