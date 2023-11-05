# def czy_pusty_csv():
#     with open(output, 'r') as csvfile:
#         csv_dict = [row for row in csv.DictReader(csvfile)]
#         if len(csv_dict) == 0:
#             return 1

# def zapisz():
#     flag = True
#     with open(output, 'w', newline='') as out_file:
#         for x in tablica:
#             writer = csv.writer(out_file, delimiter=';')
#             if czy_pusty_csv():
#                 while flag:
#                     writer.writerow(tytul_row)
#                     flag = False
#             writer.writerow(x)
#             # print (x)

# def czy_powtorzenie(szukana, wiersz):
#     licznik = 0
    
#     with open(path1, 'r') as csvfile:      #* Path1 to Stary plik 
#         csvreader = csv.reader(csvfile, delimiter =";")
#         for row in csvreader:
#             if row[4] != szukana and licznik>300:
#                 tablica.append(wiersz)
#                 break

#             elif row[4] == szukana:
#                 print("Powtorka")
#                 break

#             licznik = licznik + 1