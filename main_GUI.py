from tkinter import *
import marvel_data as mvd
import leaderboard
import json

# Global vars
character_correct = []
characters_wrong = []
characters_all = []
puntenAantal = 25

size_x = 500
size_y = 400


# Hints
def gui_hint_comic():
    """ Returns the comic hints from the Marvel API"""
    global puntenAantal
    hint = mvd.get_comic_name(character_correct)
    if hint:
        gui_hintfield["text"] = mvd.format_hint(hint)
        puntenAantal -= 3
        if puntenAantal <= 0:
            toonEindScherm()
        else:
            gui_updatescore()
    else:
        gui_hintfield["text"] = "Hint not available, no point subtracted."


def gui_hint_serie():
    """ Returns the comic hints from the Marvel API"""
    global puntenAantal
    hint = mvd.get_serie(character_correct)
    if hint:
        gui_hintfield["text"] = mvd.format_hint(hint)
        puntenAantal -= 3
        if puntenAantal <= 0:
            toonEindScherm()
        else:
            gui_updatescore()
    else:
        gui_hintfield["text"] = "Hint not available, no point subtracted."


def gui_hint_description():
    """ Returns the comic hints from the Marvel API"""
    global puntenAantal
    hint = mvd.get_character_description(character_correct)
    if hint:
        gui_hintfield["text"] = mvd.format_hint(hint)
        puntenAantal -= 3
        if puntenAantal <= 0:
            toonEindScherm()
        else:
            gui_updatescore()
    else:
        gui_hintfield["text"] = "Hint not available, no point subtracted."


def gui_hint_insameserieas():
    """ Returns the comic hints from the Marvel API"""
    global puntenAantal
    hint = mvd.char_in_same_story_as(character_correct)
    if hint:
        gui_hintfield["text"] = mvd.format_hint(hint)
        puntenAantal -= 3
        if puntenAantal <= 0:
            toonEindScherm()
        else:
            gui_updatescore()
    else:
        gui_hintfield["text"] = "Hint not available, no point subtracted."


def gui_hint_insamecomicas():
    """ Returns the comic hints from the Marvel API"""
    global puntenAantal
    hint = mvd.get_other_char_in_comic(character_correct)
    if hint:
        gui_hintfield["text"] = mvd.format_hint(hint)
        puntenAantal -= 3
        if puntenAantal <= 0:
            toonEindScherm()
        else:
            gui_updatescore()
    else:
        gui_hintfield["text"] = "Hint not available, no point subtracted."


# End Hints
def show_endscore():
    """Shows the score of the player in the endgame screen"""
    eindpunten['text'] = 'U heeft {} punten gescoord'.format(puntenAantal)


def gui_updatescore():
    """Update the current amount of points shown in GUI"""
    global puntenAantal
    puntenTeller["text"] = 'Huidige punten: {}'.format(puntenAantal)


def checkantwoord(answer):
    """Check if the given answer is correct. If so show the endscreen, else substract 5 point and update the GUI."""
    global puntenAantal
    if answer:
        toonEindScherm()
    else:
        puntenAantal -= 5
        if puntenAantal <= 0:
            toonEindScherm()
        else:
            gui_updatescore()


def toonSpeelScherm():
    """
    This function is called at the start of the game.
    It initializes and clears the game variables.
    """
    # Global vars
    global character_correct
    global characters_wrong
    global characters_all
    character_correct.clear()
    characters_wrong.clear()
    characters_all.clear()

    #  Select one correct character
    character_correct = mvd.choose_character()

    # Select random wrong character, and merge correct and wrong characters
    characters_wrong = mvd.dictionary_random_characters()
    characters_all = mvd.create_character_list(characters_wrong, character_correct)
    # Shuffel character data list
    mvd.shuffellist(characters_all)

    # Apply character names to button texts
    for i in range(0, len(characters_all)):
        (buttonLijst[i])["text"] = characters_all[i]['name']

    global puntenAantal
    global spelerNaam

    spelerNaam = viewmainmenu_entry.get()
    puntenAantal = 25
    gui_updatescore()
    viewmainmenu_entry.delete(0, END)  # Empty input field in GUI

    # Pack the correct screen
    eindSchermWin.pack_forget()
    eindSchermGameOver.pack_forget()
    viewmainmenu.pack_forget()
    speelScherm.pack()

    # Get and show the start hint
    hint = mvd.get_character_description(character_correct, mvd.get_character_name(character_correct))
    if not hint:
        hint = mvd.get_comic_name(character_correct)
    if not hint:
        hint = mvd.get_serie(character_correct)

    if hint:
        gui_hintfield["text"] = mvd.format_hint(hint)
    else:
        # Chosen character doesn't contain enough information, so the game reloads with another character
        toonSpeelScherm()


def toonEindScherm():
    """Shows different endgame screens depending on the score."""
    speelScherm.pack_forget()
    viewmainmenu.pack_forget()
    global puntenAantal
    if puntenAantal <= 0:
        eindSchermGameOver.pack()
    else:
        with open('leaderboard.json', 'r+') as file:
            topscores = json.load(file)
        leaderboard.write_score(topscores=topscores, punten=puntenAantal, naam=spelerNaam)

        show_endscore()
        eindSchermWin.pack()


def Highscores_scherm():
    with open('leaderboard.json', 'r+') as file:
        topscores = json.load(file)

    Highscores_Alltime['text'] = leaderboard.lees_score(topscores)
    Highscores_Daily['text'] = leaderboard.lees_dag(topscores)
    viewmainmenu.pack_forget()
    Highscores.pack()


def Uitleg_scherm():
    viewmainmenu.pack_forget()
    viewrules.pack()


def view_menu():
    Highscores.pack_forget()
    viewrules.pack_forget()
    speelScherm.pack_forget()
    eindSchermWin.pack_forget()
    eindSchermGameOver.pack_forget()
    viewmainmenu.pack()


root = Tk()

schermBreedte = root.winfo_reqwidth()  # schermdimensies opvragen
schermHoogte = root.winfo_reqheight()

rechtsUitlijn = int(root.winfo_screenwidth() / 2 - schermBreedte / 2)  # uitlijnen voor centreren in scherm
benedenUitlijn = int(root.winfo_screenheight() / 2 - schermHoogte / 2)

root.geometry("+{}+{}".format(rechtsUitlijn, benedenUitlijn))  # midden van scherm neerzetten
root.title("Super-Wonder-Captain")


# View Game
speelScherm = Frame(master=root, width=size_x, height=size_y)
speelScherm.pack(fill="both", expand=True)
speelScherm.configure(background='red')
speelScherm.pack_propagate(0)
gui_hintfield = Label(master=speelScherm, height=7, font=("Comic Sans MS", 9), background='red', fg='white')
gui_hintfield.pack(padx=10, pady=10)

# Hint buttons
superheldInComicMetKnop = Button(master=speelScherm, text='In comic met wie hint', command=gui_hint_insamecomicas)
superheldInComicMetKnop.place(x=70, y=155)
serieKnop = Button(master=speelScherm, text='Serie hint', command=gui_hint_serie)
serieKnop.place(x=300, y=155)

characterinverhaallijnKnop = Button(master=speelScherm, text='In verhaallijn met wie hint',
                                    command=gui_hint_insameserieas)
characterinverhaallijnKnop.place(x=70, y=195)
comicKnop = Button(master=speelScherm, text='Comic hint', command=gui_hint_comic)
comicKnop.place(x=300, y=195)

# Answer buttons
raadLabel = Label(master=speelScherm, text='Raad hieronder de superheld', font=("Comic Sans MS", 11), background='red',
                  fg='white')
raadLabel.place(x=150, y=235)
superHeldButton1 = Button(master=speelScherm, command=lambda: checkantwoord(characters_all[0]['chosen']))
superHeldButton1.place(x=70, y=265)
superHeldButton2 = Button(master=speelScherm, command=lambda: checkantwoord(characters_all[1]['chosen']))
superHeldButton2.place(x=214, y=265)
superHeldButton3 = Button(master=speelScherm, command=lambda: checkantwoord(characters_all[2]['chosen']))
superHeldButton3.place(x=358, y=265)
superHeldButton4 = Button(master=speelScherm, command=lambda: checkantwoord(characters_all[3]['chosen']))
superHeldButton4.place(x=70, y=305)
superHeldButton5 = Button(master=speelScherm, command=lambda: checkantwoord(characters_all[4]['chosen']))
superHeldButton5.place(x=214, y=305)
superHeldButton6 = Button(master=speelScherm, command=lambda: checkantwoord(characters_all[5]['chosen']))
superHeldButton6.place(x=358, y=305)

buttonLijst = []
buttonLijst.extend(
    (superHeldButton1, superHeldButton2, superHeldButton3, superHeldButton4, superHeldButton5, superHeldButton6))

menuKnop = Button(master=speelScherm, text='Hoofdmenu', command=view_menu)
menuKnop.place(x=120, y=355)
puntenTeller = Label(master=speelScherm, text='Huidige punten: 25', height=1, background='light green')
puntenTeller.place(x=280, y=355)

# View Correct answer
eindSchermWin = Frame(master=root, width=size_x, height=size_y)
eindSchermWin.pack(fill="both", expand=True)
eindSchermWin.configure(background='red')
eindSchermWin.pack_propagate(0)
eindMelding = Label(master=eindSchermWin, text='Goed geraden, gefeliciteerd!', height=3, font=("Comic Sans MS", 18),
                    background='red', fg='white')
eindMelding.pack(padx=10, pady=10)
eindpunten = Label(master=eindSchermWin, height=3, font=("Comic Sans MS", 11), background='red', fg='white')
eindpunten.pack(padx=10, pady=10)
speelKnop = Button(master=eindSchermWin, text='Opnieuw spelen', command=toonSpeelScherm)
speelKnop.pack(padx=10, pady=10)
menuKnop = Button(master=eindSchermWin, text='Hoofdmenu', command=view_menu)
menuKnop.pack(padx=10, pady=10)

# View Game Over
eindSchermGameOver = Frame(master=root, width=size_x, height=size_y)
eindSchermGameOver.pack(fill="both", expand=True)
eindSchermGameOver.configure(background='red')
eindSchermGameOver.pack_propagate(0)
eindMelding = Label(master=eindSchermGameOver, text='Geen punten meer, Game Over!', height=3,
                    font=("Comic Sans MS", 18), background='red', fg='white')
eindMelding.pack(padx=10, pady=10)
speelKnop = Button(master=eindSchermGameOver, text='Opnieuw spelen', command=toonSpeelScherm)
speelKnop.pack(padx=10, pady=10)
menuKnop = Button(master=eindSchermGameOver, text='Hoofdmenu', command=view_menu)
menuKnop.pack(padx=10, pady=10)

# View Main menu
viewmainmenu = Frame(master=root, width=size_x, height=size_y)
viewmainmenu.pack(fill="both", expand=True)
viewmainmenu.configure(background='red')
viewmainmenu.pack_propagate(0)
viewmainmenu_title = Label(master=viewmainmenu, text='Welkom bij Super-Wonder-Captain', height=3, font=("Comic Sans MS", 18),
                    background='red', fg='white')
viewmainmenu_title.pack(padx=10, pady=10)
viewmainmenu_label = Label(master=viewmainmenu, text='Enter your name:', height=1, font=("Comic Sans MS", 11), background='red',
                         fg='white')
viewmainmenu_label.pack(padx=10, pady=1)
viewmainmenu_entry = Entry(master=viewmainmenu)
viewmainmenu_entry.pack(padx=10, pady=(0, 10))
viewmainmenu_startButton = Button(master=viewmainmenu, text='Start', command=toonSpeelScherm)
viewmainmenu_startButton.pack(padx=10, pady=10)
viewmainmenu_rulesButton = Button(master=viewmainmenu, text='Uitleg', command=Uitleg_scherm)
viewmainmenu_rulesButton.pack(padx=10, pady=10)
viewmainmenu_highscoresButton = Button(master=viewmainmenu, text='Highscores', command=Highscores_scherm)
viewmainmenu_highscoresButton.pack(padx=10, pady=10)

# View instructions
viewrules = Frame(master=root, width=size_x, height=size_y)
viewrules.pack(fill="both", expand=True)
viewrules.configure(background='red')
viewrules.pack_propagate(0)
viewrules_title = Label(master=viewrules, text='Uitleg', height=3, font=("Comic Sans MS", 18), background='red', fg='white')
viewrules_title.pack(padx=10, pady=10)
viewrules_rules = Label(master=viewrules, font=("Comic Sans MS", 11),
                      text='Je begint met 25 punten\n\n-3 punten bij elke nieuwe hint die je opvraagt.\n\n-1 punt bij elke foute superheld die je hebt geraden.\n')
viewrules_rules.pack(padx=10, pady=10)
viewrules_menuButton = Button(master=viewrules, text='Menu', command=view_menu)
viewrules_menuButton.pack(padx=10, pady=10)

# View Highscores
Highscores = Frame(master=root, width=size_x, height=size_y)
Highscores.pack(fill="both", expand=True)
Highscores.configure(background='red')
Highscores.pack_propagate(0)
Highscores_title_1 = Label(master=Highscores, text='Overall highscore', height=1, font=("Comic Sans MS", 18), background='red',
                         fg='white')
Highscores_title_1.pack(padx=10, pady=(5, 5))
Highscores_Alltime = Label(master=Highscores, justify=LEFT)
Highscores_Alltime.pack(padx=1, pady=(1, 0))

Highscores_title_2 = Label(master=Highscores, text='Daily highscore', height=1, font=("Comic Sans MS", 18), background='red',
                         fg='white')
Highscores_title_2.pack(padx=10, pady=(10, 5))
Highscores_Daily = Label(master=Highscores, justify=LEFT)
Highscores_Daily.pack(padx=1, pady=(1, 0))
Highscores_menuButton = Button(master=Highscores, text='Menu', command=view_menu)
Highscores_menuButton.pack(padx=10, pady=10)

view_menu()
root.mainloop()
