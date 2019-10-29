from tkinter import *

def Highscores_scherm():
    Menu.pack_forget()
    Highscores.pack()

def Uitleg_scherm():
    Menu.pack_forget()
    Uitleg.pack()

def Menu_scherm():
    Highscores.pack_forget()
    Uitleg.pack_forget()
    Menu.pack()

def Speler_Opslaan():
    speler=speler_invoer.get()
    print(speler)
root=Tk()

Menu=Frame(master=root)
Menu.pack(fill="both", expand=True)
label=Label(master=Menu, text='Welkom bij Super-Wonder-Captain')
label.pack(pady=25)
speler_invoer=Entry(master=Menu)
speler_invoer.pack()
Start_knop=Button(master=Menu, text='Start',command=Speler_Opslaan)
Start_knop.pack(pady=5)
Uitleg_knop=Button(master=Menu, text='Uitleg',command=Uitleg_scherm)
Uitleg_knop.pack(pady=5)
Highscores_knop=Button(master=Menu, text='Highscores', command=Highscores_scherm)
Highscores_knop.pack(pady=5)

Uitleg=Frame(master=root)
Uitleg.pack(fill="both", expand=True)
Uitleg_titel=Label(master=Uitleg, text='Uitleg')
Uitleg_titel.pack(pady=15)
Uitleg_regels=Label(master=Uitleg, text='Je begint met 25 punten\n-3 punten bij elke nieuwe hint die je opvraagt.\n-1 punt bij elke foute superheld die je hebt geraden.\n')
Uitleg_regels.pack(pady=2)
Uitleg_Menu_Knop=Button(master=Uitleg, text='Menu', command=Menu_scherm)
Uitleg_Menu_Knop.pack(pady=2)

Highscores=Frame(master=root)
Highscores.pack(fill="both", expand=True)
Highscores_titel=Label(master=Highscores, text='Highscores')
Highscores_titel.pack(pady=15)

Highscores_Alltime=Label(master=Highscores, text='-\n-\n-\n-')
Highscores_Alltime.pack()

Highscores_Menu_Knop=Button(master=Highscores, text='Menu', command=Menu_scherm)
Highscores_Menu_Knop.pack(pady=2)

Menu_scherm()
Menu.mainloop()


