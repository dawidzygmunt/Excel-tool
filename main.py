from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import *
from tkinter import messagebox
import csv
import popraw 
import sys
import os
import re
from tkinterdnd2 import TkinterDnD, DND_FILES



zostalo = 0
licznikP = 0
usuniete = 0
global tablica
tablica = []
path1 = 0
path2 = 0

def directory1():
    global path1
    path1 = filedialog.askopenfilename()
    if re.findall(".csv\Z", path1):
        my_label1.config(text=path1)
    elif path1 == '':
        print ()
    else:
        error_popup("Złe rozszerzenie pliku!", "Akceptowalne rozszerzenie: .csv")

def directory2():
    global path2
    path2 = filedialog.askopenfilename()
    if re.findall(".csv\Z", path2):
        my_label2.config(text=path2)
    elif path2 == '':
        print ()
    else:
        error_popup("Złe rozszerzenie pliku!", "Akceptowalne rozszerzenie: .csv")



def operacja_csv(): #* Wczytuje plik csv do tablic a następnie odwołuje się do funkcji 'czy_powtorzenie'

    with open(path2, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter =";")
        for row in csvreader:
            szukana = row[4]

            #? POMINIECIE NAGŁÓWKA
            if row[4] == 'Tytuł operacji':
                try:
                    global tytul_row
                    tytul_row = row
                except:
                    print("Problem z nagłówkami")
            else:
                czy_powtorzenie(szukana, row)
                # czy_powtorzenie(procc_end(str(szukana)), procc_end(str(row)))


def operacja_csv_better(): #* Wczytuje plik csv do tablic a następnie odwołuje się do funkcji 'czy_powtorzenie'

    with open(path2, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter =";")
        for row in csvreader:
            szukana = row[4]

            #? POMINIECIE NAGŁÓWKA
            if row[4] == 'Tytuł operacji':
                try:
                    global tytul_row
                    tytul_row = row
                except:
                    print("Problem z nagłówkami")
            else:
                czy_powtorzenie_better(szukana, row)
                # czy_powtorzenie(procc_end(str(szukana)), procc_end(str(row)))


def procc_end(string):
    napis = re.sub(r"[\n\t\s]*", "", string)
    return napis 

def get_path(filename): #* Funkcja składowa 'drag and drop'
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return filename



def znajdz_nr_Zamowienia(napis): #* Sprawdza czy w Tytule operacji występuje numer zamówienia i czy nie zawiera błędów w zasadzie zapisu
    for i, c in enumerate(napis):
        if napis[i] == 'P':     # Jeżeli w napisie znajdzie znak 'P'
            x=i+1
            try:
                while x<i+11:       #Sprawdza czy po znaku 'P' występuje 10 liczb
                    if not napis[x].isnumeric():        #Jeżeli znak nie jest liczbą
                        break
                    elif x == i+10:      #Jeżeli po znaku 'P' wystąpiło 10 cyfr
                        dlugosc = len(napis)
                        if len(napis) == x+1 or not napis[i+11].isnumeric():        #Jeżeli ciąg znaków przekracza 10 cyfr pod rząd (tzn jest 11-sta liczba, litery się nie liczą)
                            print (napis[i:i+11])
                            return 1
                    x=x+1
            except:
                return 0
    return 0


def fix_path(string): #* Przeprowadza walidacje ścieżki po funkcji drag and drop (usuwa wąsate nawiasy)
    napis1 = string.replace("{", "")
    napis2 = napis1.replace("}", "")
    return napis2
                
                
def czy_pusty_csv(): #* Sprawdza czy wybrany plik csv jest pusty, zwraca 1 jeżeli tak
    with open(output, 'r') as csvfile:
        csv_dict = [row for row in csv.DictReader(csvfile)]
        if len(csv_dict) == 0:
            return 1

def zapisz(): #* Wykorzystuje wcześniej zapisane dane do tablicy aby zapisać niepowtórzone wiersze do pliku wyjściowego csv
    flag = True
    with open(output, 'w', newline='') as out_file:
        for x in tablica:
            writer = csv.writer(out_file, delimiter=';')
            if czy_pusty_csv():
                while flag:
                    writer.writerow(tytul_row)
                    flag = False
            writer.writerow(x)
            print (x)

def czy_powtorzenie(szukana, wiersz): #* Funckja ściśle związana z 'operacje_csv' Sprawdza czy podany tytuł występuje w starszym pliku
    licznik = 0
    global zostalo
    global usuniete



    file = open(path1)
    row_count = sum(1 for row in file)
    file.close()

    with open(path1, 'r') as csvfile:      #* Path1 to Stary plik 
        csvreader = csv.reader(csvfile, delimiter =";")
        for row in csvreader:
            if (row[4]) != szukana and licznik>=row_count-1:
                tablica.append(wiersz)
                zostalo = zostalo+1
                break

            elif row[4] == szukana:
                print("Powtorka")
                usuniete= usuniete+1
                break

            licznik = licznik + 1

def czy_powtorzenie_better(szukana, wiersz): #* Funckja ściśle związana z 'operacje_csv' Sprawdza czy podany tytuł występuje w starszym pliku, ulepszona
    licznik = 0
    global zostalo
    global usuniete



    file = open(path1)
    row_count = sum(1 for row in file)
    file.close()

    with open(path1, 'r') as csvfile:      #* Path1 to Stary plik 
        csvreader = csv.reader(csvfile, delimiter =";")
        for row in csvreader:
            row_str = procc_end(str(row[4]))
            szukana_str = procc_end(str(szukana))
            if row_str != szukana_str and licznik>=row_count-1:
                tablica.append(wiersz)
                zostalo = zostalo+1
                break

            elif row_str == szukana_str:
                print("Powtorka")
                usuniete= usuniete+1
                break

            licznik = licznik + 1


def zatwierdzanie_nr(): #* Funkcja akutalnie nic nie robi, aktywowana jest po zatwierdzeniu zmian w numerze zamówienia (Nie dodane)
    print()



def podsumowanie(): #* Wyświetla ekran podsumowania
    global top
    top = Toplevel(root)
    top.geometry("460x170")
    top.title("Opracja zakończyla się sukcesem!")
    top.iconbitmap(get_path("ok.ico"))
    

    #? STYLE
    st = Style()
    st.configure('b1.TButton', font='helvetica 14 bold', padding=5)
    st.configure('b2.TButton', font='helvetica 14 bold', padding=5)


    Label(top, text="Usunięto " + str(usuniete) + " wierszy", font=('Calibri 14')).place(relx=0.02, rely=0.05, anchor=NW)
    Label(top, text="Pozostało " + str(zostalo) + " rekordów", font=('Calibri 14')).place(relx=0.02, rely=0.25, anchor=W)

    Label(top, text="Błędne tytuły: " + str(licznikP), font=('Calibri 14 bold')).place(relx=0.6, rely=0.10, anchor=W)
    Button(top, text="Zatwierdź", padding=2, command=zatwierdzanie_nr).place(relx=0.65, rely=0.25)

    Button(top, text="Importuj nowy", style='b1.TButton', command=restart).place(relx=0.15, rely=0.58)
    Button(top, text="Zamknij", style='b2.TButton', command=close).place(relx=0.56, rely=0.58)



def close(): #* Zamyka program
    root.destroy()

def restart(): #* Resetuje zmienne po wciśnięciu przycisku Importuj nowy
    top.destroy()
    global zostalo
    global licznikP
    global usuniete
    global tablica
    global path1
    global path2
    zostalo = 0
    licznikP = 0
    usuniete = 0
    tablica = []
    path1 = 0
    path2 = 0

    my_label1.configure(text="Wybierz loalizacje pliku csv")
    my_label2.configure(text="Wybierz loalizacje pliku csv")




def error_popup(tytul, text): #* Wyświetla pop-up z treścią błędu
    messagebox.showerror(tytul, text)


def submit():
    if czyPoprawic.get() == 1: #* Jeżeli opcja popraw odstępy jest zaznaczona (tymcz. wyłączone)
        print ("zaznaczono opcje")
        global output
        if not path1 or not path2: #? Jeżeli nie wybrano pliku CSV
            error_popup("Brak ścieżki do pliku!", "Nie wybrano pliku CSV")
        else:
            FILES=[("CSV Files", "*.csv")]
            output = filedialog.asksaveasfilename(filetypes = FILES, defaultextension=FILES)

        if output:
            operacja_csv_better()
            zapisz()
        
            global licznikP
            for x in tablica:
                if znajdz_nr_Zamowienia(x[4]) == 0:
                    licznikP = licznikP + 1

            podsumowanie()

            
    else:   #* Jeżeli opcja nie została zaznaczona (domyślnie)
        print ("opcja 0")
        if not path1 or not path2:
            error_popup("Brak ścieżki do pliku!", "Nie wybrano pliku CSV")   #! PAMIETAJ ZMIENIC NA ERROR_POPUP !!!!!!!!!!!!!!!!
        else:
            FILES=[("CSV Files", "*.csv")]
            output = filedialog.asksaveasfilename(filetypes = FILES, defaultextension=FILES)
            
            if output:
                print ("poszlo")
                operacja_csv()
                zapisz()

                for x in tablica:   # Liczy ilość wystąpień błędów w numerze zamówienia
                    if znajdz_nr_Zamowienia(x[4]) == 0:
                        licznikP = licznikP + 1

                podsumowanie()




def path_listbox1(event):   #* drag and drop zmiennia parametry dla path1
    global path1
    sciezka = fix_path(event.data)

    #* Walidacja danych
    if re.findall(".csv\Z", sciezka):
        my_label1.config(text=sciezka)
        path1 = sciezka
    elif sciezka == '':
        print ()
    else:
        error_popup("Złe rozszerzenie pliku!", "Akceptowalne rozszerzenie: .csv")

def path_listbox2(event):   #* drag and drop zmiennia parametry dla path2
    global path2
    sciezka = fix_path(event.data)
    my_label2.configure(text=sciezka)
    path2 = sciezka


root = TkinterDnD.Tk()
root.title("Cutterspace CSV")
root.geometry("860x150")
root.iconbitmap(get_path("logo.ico"))
czyPoprawic = IntVar()

    #? STYLE 
st = Style()
st.configure('submit.TButton', font='helvetica 14 bold', padding=5)
st.configure("fun.TLabel", background="white", width="108", text='List', anchor="ceter")


mainframe = ttk.Frame(root, padding="16 16 6 6")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=6)
root.rowconfigure(0, weight=1)
my_label1 = Label(mainframe, text="Wybierz loalizacje pliku csv", style="fun.TLabel")
my_label2 = Label(mainframe, text="Wybierz loalizacje pliku csv", style='fun.TLabel')


ttk.Label(mainframe, text="Stary plik: ").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Nowy plik: ").grid(column=1, row=2, sticky=W)


my_label1.grid(column=2, row=1)
my_label1.drop_target_register(DND_FILES)
my_label1.dnd_bind('<<Drop>>', path_listbox1)
my_label2.grid(column=2, row=2)
my_label2.drop_target_register(DND_FILES)
my_label2.dnd_bind('<<Drop>>', path_listbox2)


ttk.Button(mainframe, text="Wybierz", command=directory1).grid(column=3, row=1, sticky=W)
ttk.Button(mainframe, text="Wybierz", command=directory2).grid(column=3, row=2, sticky=W)


czyPoprawic = IntVar()
ttk.Checkbutton(mainframe, text='Better format +', variable=czyPoprawic, onvalue=1, offvalue=0).grid(column=2, row=3, sticky=NW)
ttk.Button(mainframe, text="Zatwierdź", style='submit.TButton', command=submit).grid(column=2, row=3, sticky=SE)
ttk.Label(mainframe, text="v1.1").grid(column=1, row=3, sticky=SW, padx=5)



for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()