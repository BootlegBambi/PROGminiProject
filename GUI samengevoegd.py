from tkinter import *
from tkinter.messagebox import showinfo #popup
import GUI_Knoppen_Functies as GUI_fnc
from random import shuffle

def nieuweHint():
    hint = 'Nieuwe hint vanuit API opgehaald'
    beginHint["text"] = hint #straks vanuit api dus random
    global puntenAantal
    puntenAantal-= 3 #puntenaftrek voor hint
    if puntenAantal <= 0:
        toonEindScherm() #geen hints meer, eindscherm
    else:
        puntenUpdate()

def puntenUpdate():
    puntenTekst = 'Huidige punten: {}'
    puntenTeller["text"] = puntenTekst.format(puntenAantal) #punten updaten in speelscherm

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

def toonSpeelScherm():
    superheldenLijst.append(goeieSuperheld) #global goeie antwoord toevoegen ivm anders meerdere functiecalls
    for i in range(0, 5):
        superheldenLijst.append(GUI_fnc.buttonSuperheld())
    shuffle(superheldenLijst)
    global puntenAantal
    puntenAantal = 25
    puntenUpdate()
    global speler_invoer
    speler_invoer.delete(0, END) #spelerentry legen
    eindSchermWin.pack_forget()
    eindSchermGameOver.pack_forget()
    Menu.pack_forget()
    speelScherm.pack()
    beginHint["text"] = 'Teruggezet op nieuwe beginhint'
    speler = speler_invoer.get() #!!naar bestand voor highscores schrijven


def toonEindScherm(): #!!aanpassen: huidige puntenaantal opslaan in highscorelijst
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
superheldenLijst = []
goeieSuperheld = GUI_fnc.buttonAntwoord()

#scherm tijdens het spelen
speelScherm = Frame(master=root, width = 500, height = 300)
speelScherm.pack(fill = "both", expand = True)
speelScherm.pack_propagate(0)
beginHint = Label(master=speelScherm, text = 'deze tekst maakt waarschijnlijk niet meer uit', height = 1,background='yellow')
beginHint.pack(padx = 10, pady = 10)

#meerdere buttons aanmaken voor verschillende hints
#true/false variabele voor knop al gedrukt of niet
#hint ophalen vanuit API, één hint per keer simpel printen, overschrijven want true/false variabele
hintKnop = Button(master=speelScherm, text='Nieuwe hint opvragen', command=nieuweHint)
hintKnop.pack(padx=10, pady=5)
raadLabel = Label(master=speelScherm, text='Raad hieronder de superheld')
raadLabel.pack(padx=10, pady=5)

#lijst maken en shuffelen van namen
#for loop doorlopen x[tekst] = superheldnaam
#bij command functie voor if superheldnaam = tekst dan goed anders -1

superHeldButton1 = Button(master=speelScherm, text = 'superheld 1')
superHeldButton1.place(x = 70, y = 120)
superHeldButton2 = Button(master=speelScherm, text = 'superheld 2')
superHeldButton2.place(x = 214, y = 120) #length = 72px
superHeldButton3 = Button(master=speelScherm, text = 'superheld 3')
superHeldButton3.place(x = 358, y = 120)
superHeldButton4 = Button(master=speelScherm, text = 'superheld 4')
superHeldButton4.place(x = 70, y = 160)
superHeldButton5 = Button(master=speelScherm, text = 'superheld 5')
superHeldButton5.place(x = 214, y = 160)
superHeldButton6 = Button(master=speelScherm, text = 'superheld 6')
superHeldButton6.place(x = 358, y = 160)

menuKnop = Button(master=speelScherm, text = 'Hoofdmenu', command = Menu_scherm)
menuKnop.place(x = 120, y = 210)
puntenTeller = Label(master=speelScherm, text = 'Huidige punten: 25', height = 1)
puntenTeller.place(x = 280, y = 210)

#scherm als goed geraden
eindSchermWin = Frame(master=root, width = 500, height = 300)
eindSchermWin.pack(fill="both", expand = True)
eindSchermWin.pack_propagate(0)
eindMelding = Label(master=eindSchermWin, text = 'Goed geraden, gefeliciteerd!.', height = 3)
eindMelding.pack(padx = 10, pady = 10)
speelKnop = Button(master=eindSchermWin, text='Opnieuw spelen', command=toonSpeelScherm)
speelKnop.pack(padx=10, pady=10)
menuKnop = Button(master=eindSchermWin, text = 'Hoofdmenu', command = Menu_scherm)
menuKnop.pack(padx = 10, pady = 10)

#scherm als game over
eindSchermGameOver = Frame(master=root, width = 500, height = 300)
eindSchermGameOver.pack(fill="both", expand = True)
eindSchermGameOver.pack_propagate(0)
eindMelding = Label(master=eindSchermGameOver, text = 'Geen punten meer, Game Over.', height = 3)
eindMelding.pack(padx = 10, pady = 10)
speelKnop = Button(master=eindSchermGameOver, text='Opnieuw spelen', command=toonSpeelScherm)
speelKnop.pack(padx=10, pady=10)
menuKnop = Button(master=eindSchermGameOver, text = 'Hoofdmenu', command = Menu_scherm)
menuKnop.pack(padx = 10, pady = 10)

#menuscherm
Menu=Frame(master=root, width=500, height=300)
Menu.pack(fill="both", expand=True)
Menu.pack_propagate(0)
label=Label(master=Menu, text='Welkom bij Super-Wonder-Captain', height = 3)
label.pack(padx = 10, pady = 10)
speler_invoer=Entry(master=Menu)
speler_invoer.pack(padx = 10, pady = 10)
Start_knop=Button(master=Menu, text='Start',command=toonSpeelScherm)
Start_knop.pack(padx = 10, pady = 10)
Uitleg_knop=Button(master=Menu, text='Uitleg',command=Uitleg_scherm)
Uitleg_knop.pack(padx = 10, pady = 10)
Highscores_knop=Button(master=Menu, text='Highscores', command=Highscores_scherm)
Highscores_knop.pack(padx = 10, pady = 10)

#uitlegscherm
Uitleg=Frame(master=root, width=500, height=300)
Uitleg.pack(fill="both", expand=True)
Uitleg.pack_propagate(0)
Uitleg_titel=Label(master=Uitleg, text='Uitleg', height = 3)
Uitleg_titel.pack(padx = 10, pady = 10)
Uitleg_regels=Label(master=Uitleg, text='Je begint met 25 punten\n-3 punten bij elke nieuwe hint die je opvraagt.\n-1 punt bij elke foute superheld die je hebt geraden.\n')
Uitleg_regels.pack(padx = 10, pady = 10)
Uitleg_Menu_Knop=Button(master=Uitleg, text='Menu', command=Menu_scherm)
Uitleg_Menu_Knop.pack(padx = 10, pady = 10)

#highscorescherm
Highscores=Frame(master=root, width=500, height=300)
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