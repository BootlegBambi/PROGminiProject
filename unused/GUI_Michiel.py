from tkinter import *
from tkinter.messagebox import showinfo #popup

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
    pogingInvoer = raadVeld.get()
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
    global puntenAantal
    puntenAantal = 25
    puntenUpdate()
    global raadVeld
    raadVeld.delete(0, END) #tekstvak leegmaken van vorige entry
    eindSchermWin.pack_forget()
    eindSchermGameOver.pack_forget()
    hoofdMenuScherm.pack_forget()
    speelScherm.pack()

def toonEindScherm(): #!!aanpassen: huidige puntenaantal opslaan in highscorelijst
    speelScherm.pack_forget()
    hoofdMenuScherm.pack_forget()
    global puntenAantal
    if puntenAantal <= 0:
        eindSchermGameOver.pack()
    else:
        eindSchermWin.pack()

def toonHoofdMenu():
    speelScherm.pack_forget()
    eindSchermWin.pack_forget()
    eindSchermGameOver.pack_forget()
    hoofdMenuScherm.pack()

root = Tk()

schermBreedte = root.winfo_reqwidth() #schermdimensies opvragen
schermHoogte = root.winfo_reqheight()

rechtsUitlijn = int(root.winfo_screenwidth() / 2 - schermBreedte / 2) #uitlijnen voor centreren in scherm
benedenUitlijn = int(root.winfo_screenheight() / 2 - schermHoogte / 2)

root.geometry("+{}+{}".format(rechtsUitlijn, benedenUitlijn)) #midden van scherm neerzetten

puntenAantal = 25

#scherm tijdens het spelen
speelScherm = Frame(master=root, width = 500, height = 300)
speelScherm.pack(fill = "both", expand = True)
speelScherm.pack_propagate(0)
beginHint = Label(master=speelScherm, text = 'Dit is de beginhint voor elke nieuwe speler', height = 3)
beginHint.pack(padx = 10, pady = 10)
raadVeld = Entry(master=speelScherm)
raadVeld.pack(padx = 10, pady = 10)
raadKnop = Button(master=speelScherm, text = 'Bevestigen', command = raadPoging)
raadKnop.pack(padx = 10, pady = 10)
hintKnop = Button(master=speelScherm, text = 'Hint opvragen', command = nieuweHint)
hintKnop.pack(padx = 10, pady = 10)
stopKnop = Button(master=speelScherm, text = 'Hoofdmenu', command = toonHoofdMenu)
stopKnop.pack(padx = 10, pady = 10)
puntenTeller = Label(master=speelScherm, text = 'Huidige punten: 25', height = 3)
puntenTeller.pack(padx = 10, pady = 10)

#scherm als goed geraden
eindSchermWin = Frame(master=root, width = 500, height = 300)
eindSchermWin.pack(fill="both", expand = True)
eindSchermWin.pack_propagate(0)
eindMelding = Label(master=eindSchermWin, text = 'Goed geraden, gefeliciteerd!.', height = 3)
eindMelding.pack(padx = 10, pady = 10)
speelKnop = Button(master=eindSchermWin, text='Opnieuw spelen', command=toonSpeelScherm)
speelKnop.pack(padx=10, pady=10)
menuKnop = Button(master=eindSchermWin, text = 'Hoofdmenu', command = toonHoofdMenu)
menuKnop.pack(padx = 10, pady = 10)

#scherm als game over
eindSchermGameOver = Frame(master=root, width = 500, height = 300)
eindSchermGameOver.pack(fill="both", expand = True)
eindSchermGameOver.pack_propagate(0)
eindMelding = Label(master=eindSchermGameOver, text = 'Geen punten meer, Game Over.', height = 3)
eindMelding.pack(padx = 10, pady = 10)
speelKnop = Button(master=eindSchermGameOver, text='Opnieuw spelen', command=toonSpeelScherm)
speelKnop.pack(padx=10, pady=10)
menuKnop = Button(master=eindSchermGameOver, text = 'Hoofdmenu', command = toonHoofdMenu)
menuKnop.pack(padx = 10, pady = 10)

#hoofdmenuscherm
hoofdMenuScherm = Frame(master=root, width = 500, height = 300)
hoofdMenuScherm.pack(fill="both", expand = True)
hoofdMenuScherm.pack_propagate(0)
welkomMelding = Label(master=hoofdMenuScherm, text = 'Welkom bij Super-Wonder-Captain!', height = 3)
welkomMelding.pack(padx = 10, pady = 10)
speelKnop2 = Button(master=hoofdMenuScherm, text = 'Start', command = toonSpeelScherm)
speelKnop2.pack(padx = 10, pady = 10)

toonHoofdMenu()
root.mainloop()