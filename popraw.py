# def czy_numer(liczba):
#     if liczba.isnumeric():
#         return 1


# def wstepny_processing(napis):
#     output = []
#     output = napis.split()
#     for x in output:
#         print (x)
#         usuwanie_spacji(x)



def znajdz_nr_Zamowienia(napis):
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

# def znajdz_nrZamowienia_spacja(napis):
#     for i, c in enumerate(napis):
#         if napis[i] == 'P' and napis[i+1] == " ":    # Jeżeli w napisie znajdzie znak 'P' oraz następny znak to spacja
#             x=i+1
#             if napis[x] == " ":      #Zwiększa zmienną x o jeden aby pomiąć sprawdzanie spacji, jeżeli znakiem po 'P' jest spacja 
#                 x=x+1
#             try:
#                 while x<i+12:       #Sprawdza czy po znaku 'P' występuje 10 liczb
#                     if not napis[x].isnumeric():    #Jeżeli znak nie jest liczbą
#                         break
#                     elif x == i+11:     #Jeżeli po znaku 'P' wystąpiło 10 cyfr
#                         dlugosc = len(napis)
#                         if dlugosc == x+1 or not napis[i+12].isnumeric():       #Jeżeli ciąg znaków nie przekracza 10 cyfr pod rząd (tzn jest 11-sta liczba, litery się nie liczą)
#                             usuwanie_spacji(napis, i)
#                             return napis[i:i+12]
#                     x=x+1
#             except:
#                 return 0
#     return 0



# def usuwanie_spacji(napis):
#     nowy = napis.replace(" ", "")
#     out = znajdz_nrZamowienia(nowy)

            




# # usuwanie_spacji("01 P 0123456789")
# zmienna = wstepny_processing("Ala ma kota")
# print (zmienna)



            
        
