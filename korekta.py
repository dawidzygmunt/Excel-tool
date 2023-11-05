import re


def rozdziel_spacje(text):
    x = text.split()
    return x
    


def znajdz_nr(text):
    if re.findall("[P]\d\d\d\d\d\d\d\d\d\d\Z", text) or re.findall("[P]\d\d\d\d\d\d\d\d\d\d\D", text):
        if re.findall("[P]\d\d\d\d\d\d\d\d\d\d\Z", text):
            x = re.findall("[P]\d\d\d\d\d\d\d\d\d\d\Z", text)
            resault = re.sub("[P]\d\d\d\d\d\d\d\d\d\d", usuwanie_spacji(x), text)
            return None
        elif re.findall("[P]\d\d\d\d\d\d\d\d\d\d\D", text):
            x = re.findall("[P]\d\d\d\d\d\d\d\d\d\d", text)
            resault = re.sub("[P]\d\d\d\d\d\d\d\d\d\d", usuwanie_spacji(x), text)
            return resault

    elif re.findall("[P]\s\d\d\d\d\d\d\d\d\d\d\Z", text) or re.findall("[P]\s\d\d\d\d\d\d\d\d\d\d\D", text):
        x = re.findall("[P]\s\d\d\d\d\d\d\d\d\d\d\Z", text)
        print("2")
        resault = re.sub("[P]\s\d\d\d\d\d\d\d\d\d\d", usuwanie_spacji(x), text)
        return resault

    elif re.findall("[P]\s\s\d\d\d\d\d\d\d\d\d\d\Z", text) or re.findall("[P]\s\s\d\d\d\d\d\d\d\d\d\d\D", text):
        x = re.findall("[P]\s\s\d\d\d\d\d\d\d\d\d\d", text)
        print("3")
        resault = re.sub("[P]\s\s\d\d\d\d\d\d\d\d\d\d", usuwanie_spacji(x), text)
        return resault

    if re.findall("[P]\s\s\s\d\d\d\d\d\d\d\d\d\d\Z", text) or re.findall("[P]\s\s\s\d\d\d\d\d\d\d\d\d\d\D", text):
        x = re.findall("[P]\s\s\s\d\d\d\d\d\d\d\d\d\d", text)
        resault = re.sub("[P]\s\s\s\d\d\d\d\d\d\d\d\d\d", usuwanie_spacji(x), text)
        print("4")
        return resault
    


def usuwanie_spacji(napis):
    x = str(napis).replace(" ", "")
    x1 = str(x).replace("[", " ")
    x2 = str(x1).replace("]", " ")
    x3 = str(x2).replace("'", "")
    return str(x3)







if znajdz_nr(testowy_napis):
    znaleziony_napis = znajdz_nr(testowy_napis)
    output = usuwanie_spacji (znaleziony_napis)
    print (output)
else:
    print ("hw")


   
   
def fix_path(string):
    napis1 = string.replace("{", "")
    napis2 = napis1.replace("}", "")
    return napis2

