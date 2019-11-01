from tkinter import *
from tkinter.messagebox import showinfo
import marvel_data as mvd

# Global vars
character_correct = []
characters_wrong = []
characters_all = []

size_x = 500
size_y = 400




# Hints
def gui_hint_comic():
    """ Returns the comic hints from the Marvel API"""
    global puntenAantal
    hint = mvd.get_comic_name(character_correct)
    if hint:
        gui_hintfield["text"] = hint
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
        gui_hintfield["text"] = hint
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
        gui_hintfield["text"] = hint
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
        gui_hintfield["text"] = hint
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
        gui_hintfield["text"] = hint
        puntenAantal -= 3
        if puntenAantal <= 0:
            toonEindScherm()
        else:
            gui_updatescore()
    else:
        gui_hintfield["text"] = "Hint not available, no point subtracted."
# End Hints

def checkscore():

    return

def gui_updatescore():
    """Update the current amount of points shown in GUI"""
    puntenTekst = 'Huidige punten: {}'
    puntenTeller["text"] = puntenTekst.format(puntenAantal)


def raadPoging():
    pogingInvoer = 'lol'#TIJDELIJK TOTDAT DE MEERKEUZE IS INGEVOEGD
    if pogingInvoer == 'test': #!!aanpassen: punten naar highscore schrijven, score resetten
        toonEindScherm()
    else:
        showinfo(title='popup', message='Verkeerd geraden') #popup voor verkeerd geraden + puntenaftrek
        global puntenAantal
        puntenAantal-= 1
        if puntenAantal <= 0:
            toonEindScherm()
        else:
            puntenUpdate()


def checkantwoord(answer):
    if answer:
        toonEindScherm()


def toonSpeelScherm():
    """This function is called at the start of the game"""
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
    global gui_speler_invoer

    puntenAantal = 25
    gui_updatescore()
    gui_speler_invoer.delete(0, END)  # Empty input field in GUI

    # Pack the correct screen
    eindSchermWin.pack_forget()
    eindSchermGameOver.pack_forget()
    Menu.pack_forget()
    speelScherm.pack()

    # Get and show the start hint
    try:
        hint = mvd.get_character_description(character_correct, mvd.get_character_name(character_correct))
        if not hint:
            hint = mvd.get_comic_name(character_correct)
        if not hint:
            hint = mvd.get_serie(character_correct)

        gui_hintfield["text"] = mvd.format_hint(hint)
    except:
        showinfo(title='Play again', message="Randomly chosen superhero doesn't contain enough meta information for this program to work.")
        Menu_scherm()


def toonEindScherm():
    speelScherm.pack_forget()
    Menu.pack_forget()
    global puntenAantal
    if puntenAantal <= 0:
        eindSchermGameOver.pack()
    else:
        eindSchermWin.pack()

def Highscores_scherm():
    Menu.pack_forget()
    Highscores.pack()

def Uitleg_scherm():
    Menu.pack_forget()
    Uitleg.pack()

def Menu_scherm():
    Highscores.pack_forget()
    Uitleg.pack_forget()
    speelScherm.pack_forget()
    eindSchermWin.pack_forget()
    eindSchermGameOver.pack_forget()
    Menu.pack()


root = Tk()

schermBreedte = root.winfo_reqwidth() #schermdimensies opvragen
schermHoogte = root.winfo_reqheight()

rechtsUitlijn = int(root.winfo_screenwidth() / 2 - schermBreedte / 2) #uitlijnen voor centreren in scherm
benedenUitlijn = int(root.winfo_screenheight() / 2 - schermHoogte / 2)

root.geometry("+{}+{}".format(rechtsUitlijn, benedenUitlijn)) #midden van scherm neerzetten

puntenAantal = 25

#scherm tijdens het spelen
speelScherm = Frame(master=root, width = size_x, height = size_y)
speelScherm.pack(fill = "both", expand = True)
speelScherm.pack_propagate(0)
gui_hintfield = Label(master=speelScherm, height=7, background='yellow')
gui_hintfield.pack(padx=10, pady=10)

#meerdere buttons aanmaken voor verschillende hints
#true/false variabele voor knop al gedrukt of niet
#hint ophalen vanuit API, één hint per keer simpel printen, overschrijven want true/false variabele
comicKnop = Button(master=speelScherm, text='Comic hint', command=gui_hint_comic)
comicKnop.place(x = 70, y = 155)
serieKnop = Button(master=speelScherm, text='Serie hint', command=gui_hint_serie)
serieKnop.place(x = 190, y = 155)
characterinverhaallijnKnop = Button(master=speelScherm, text='In verhaallijn met wie hint', command=gui_hint_insameserieas)
characterinverhaallijnKnop.place(x = 285, y = 155)
superheldInComicMetKnop = Button(master=speelScherm, text='In comic met wie hint', command=gui_hint_insamecomicas)
superheldInComicMetKnop.place(x = 305, y = 195)
DescriptionKnop = Button(master=speelScherm, text='Description superheld', command=gui_hint_description)
DescriptionKnop.place(x = 70, y = 195)

raadLabel = Label(master=speelScherm, text='Raad hieronder de superheld',background='orange')
raadLabel.place(x=172, y=235)

#lijst maken en shuffelen van namen
#for loop doorlopen x[tekst] = superheldnaam
#bij command functie voor if superheldnaam = tekst dan goed anders -1


superHeldButton1 = Button(master=speelScherm, command=lambda: checkantwoord(characters_all[0]['chosen']))
superHeldButton1.place(x = 70, y = 265)
superHeldButton2 = Button(master=speelScherm, command=lambda: checkantwoord(characters_all[1]['chosen']))
superHeldButton2.place(x = 214, y = 265) #length = 72px
superHeldButton3 = Button(master=speelScherm, command=lambda: checkantwoord(characters_all[2]['chosen']))
superHeldButton3.place(x = 358, y = 265)
superHeldButton4 = Button(master=speelScherm, command=lambda: checkantwoord(characters_all[3]['chosen']))
superHeldButton4.place(x = 70, y = 305)
superHeldButton5 = Button(master=speelScherm, command=lambda: checkantwoord(characters_all[4]['chosen']))
superHeldButton5.place(x = 214, y = 305)
superHeldButton6 = Button(master=speelScherm, command=lambda: checkantwoord(characters_all[5]['chosen']))
superHeldButton6.place(x = 358, y = 305)

buttonLijst = []
buttonLijst.extend((superHeldButton1, superHeldButton2, superHeldButton3, superHeldButton4, superHeldButton5, superHeldButton6))

menuKnop = Button(master=speelScherm, text = 'Hoofdmenu', command = Menu_scherm)
menuKnop.place(x = 120, y = 355)
puntenTeller = Label(master=speelScherm, text = 'Huidige punten: 25', height = 1,background='light green')
puntenTeller.place(x = 280, y = 355)

#scherm als goed geraden
eindSchermWin = Frame(master=root, width = size_x, height = size_y)
eindSchermWin.pack(fill="both", expand = True)
eindSchermWin.pack_propagate(0)
eindMelding = Label(master=eindSchermWin, text = 'Goed geraden, gefeliciteerd!', height = 3)
eindMelding.pack(padx = 10, pady = 10)
eindpunten = Label(master=eindSchermWin, text='Uw heeft {} punten gescoord'.format(puntenAantal), height=3)
eindpunten.pack(padx = 10, pady = 10)
speelKnop = Button(master=eindSchermWin, text='Opnieuw spelen', command=toonSpeelScherm)
speelKnop.pack(padx=10, pady=10)
menuKnop = Button(master=eindSchermWin, text = 'Hoofdmenu', command = Menu_scherm)
menuKnop.pack(padx = 10, pady = 10)

#scherm als game over
eindSchermGameOver = Frame(master=root, width = size_x, height = size_y)
eindSchermGameOver.pack(fill="both", expand = True)
eindSchermGameOver.pack_propagate(0)
eindMelding = Label(master=eindSchermGameOver, text = 'Geen punten meer, Game Over.', height = 3)
eindMelding.pack(padx = 10, pady = 10)
speelKnop = Button(master=eindSchermGameOver, text='Opnieuw spelen', command=toonSpeelScherm)
speelKnop.pack(padx=10, pady=10)
menuKnop = Button(master=eindSchermGameOver, text = 'Hoofdmenu', command = Menu_scherm)
menuKnop.pack(padx = 10, pady = 10)

#menuscherm
Menu=Frame(master=root, width=size_x, height=size_y)
Menu.pack(fill="both", expand=True)
Menu.configure(background='red')
Menu.pack_propagate(0)
label=Label(master=Menu, text='Welkom bij Super-Wonder-Captain', height = 3)
label.pack(padx = 10, pady = 10)
gui_speler_invoer=Entry(master=Menu)
gui_speler_invoer.pack(padx = 10, pady = 10)
Start_knop=Button(master=Menu, text='Start',command=toonSpeelScherm)
Start_knop.pack(padx = 10, pady = 10)
Uitleg_knop=Button(master=Menu, text='Uitleg',command=Uitleg_scherm)
Uitleg_knop.pack(padx = 10, pady = 10)
Highscores_knop=Button(master=Menu, text='Highscores', command=Highscores_scherm)
Highscores_knop.pack(padx = 10, pady = 10)

#uitlegscherm
Uitleg=Frame(master=root, width=size_x, height=size_y)
Uitleg.pack(fill="both", expand=True)
Uitleg.pack_propagate(0)
Uitleg_titel=Label(master=Uitleg, text='Uitleg', height = 3)
Uitleg_titel.pack(padx = 10, pady = 10)
Uitleg_regels=Label(master=Uitleg, text='Je begint met 25 punten\n-3 punten bij elke nieuwe hint die je opvraagt.\n-1 punt bij elke foute superheld die je hebt geraden.\n')
Uitleg_regels.pack(padx = 10, pady = 10)
Uitleg_Menu_Knop=Button(master=Uitleg, text='Menu', command=Menu_scherm)
Uitleg_Menu_Knop.pack(padx = 10, pady = 10)

#highscorescherm
Highscores=Frame(master=root, width=size_x, height=size_y)
Highscores.pack(fill="both", expand=True)
Highscores.pack_propagate(0)
Highscores_titel=Label(master=Highscores, text='Highscores', height = 3)
Highscores_titel.pack(padx = 10, pady = 10)
Highscores_Alltime=Label(master=Highscores, text='-\n-\n-\n-')
Highscores_Alltime.pack(padx = 10, pady = 10)
Highscores_Menu_Knop=Button(master=Highscores, text='Menu', command=Menu_scherm)
Highscores_Menu_Knop.pack(padx = 10, pady = 10)

Menu_scherm()
root.mainloop()