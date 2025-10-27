import random
def karten_ziehen(anzahl):
    auswertung=[]
    # geht alles schneller mit return random.sample(range(1, 53), anzahl)
    while len(auswertung)<anzahl:
        zahl = random.randint(1, 52)
        if zahl not in auswertung:
            auswertung.append(zahl)
    return auswertung
def kombination(karten):
    farben=[]
    werte=[]
    for i in range(len(karten)):
        farbe=(karten[i]-1)//13 # mit -1
        wert=(karten[i]-1)%13
        farben.append(farbe)
        werte.append(wert)
    #print(farben)
    #print(werte)
    #Prüfen
    if royal_flush(farben, werte):
        return 9
    if straight_flush(farben, werte):
        return 8
    if quattet(farben, werte):
        return 7
    if full_house(farben, werte):
        return 6
    if flush(farben, werte):
        return 5
    if straight(farben, werte):
        return 4
    if triplett(farben, werte):
        return 3
    if two_pair(farben, werte):
        return 2
    if pair(farben, werte):
        return 1
    else:
        return 0

def pair(farben, werte):
    if (len(set(werte))<len(werte)):
        return True
    return False

def two_pair(farben, werte):
    if (len(set(werte))<=len(werte)-2):

        return True
    return False

def triplett(farben, werte):
    werte=simple_sort(werte)
    if (len(set(werte))<=len(werte)-2):
        if (werte[0] == werte[1] == werte[2]) or (werte[2] == werte[3] == werte[4]) or (werte[1]==werte[2]==werte[3]):
            return True
    return False

def straight(farben, werte):
    werte=simple_sort(werte)
    #print(werte)
    for i in range(0,len(werte)-1):
        if werte[i] != werte[i+1]-1:
            return False
    return True

def flush(farben, werte):
    if (len(set(farben))==1):
        return True
    return False

def full_house (farben, werte):
    if len(set(werte)) <= len(werte) - 3:
        werte=simple_sort(werte)
        if werte[0] == werte[1] and werte[len(werte) - 1]== werte[len(werte) - 2]:
            return True
    return False

def quattet(farben, werte):
    if len(set(werte))<=len(werte)-3:
        werte=simple_sort(werte)
        if (werte[0]==werte[1]==werte[2]==werte[3]) or (werte[1]==werte[2]==werte[3]==werte[4]):
            return True
    return False

def straight_flush(farben, werte):
    werte=simple_sort(werte)
    # print(werte)
    for i in range(0, len(werte) - 1):
        if werte[i] != werte[i + 1] - 1:
            return False
    if (len(set(farben))==1):
        return True
    else:
        return False

def royal_flush(farben, werte):
    werte=simple_sort(werte)
    if (len(set(farben))==1):
        if (werte[0] ==0 and werte[1]==9 and werte[2]==10 and werte[3]==11 and werte[4]==12):
            return True
    return False

def absolute_zahlen_berechnen(anzahl):
    ergebnis={}
    for i in range(0,10):
        ergebnis[i]=0
    for i in range(0,anzahl):
        ziehung = (karten_ziehen(5))
        kombinations_nummer = kombination(ziehung)
        ergebnis[kombinations_nummer]=ergebnis[kombinations_nummer]+1
    return ergebnis

def prozentual_ausrechnen(anzahl):
    absolute_zahlen = absolute_zahlen_berechnen(anzahl)
    print(absolute_zahlen)
    for i in range(len(absolute_zahlen)):
        absolute_zahlen[i]=absolute_zahlen[i]/anzahl*100
    return absolute_zahlen

def simple_sort(array):
    for i in range(len(array)-1):
        #print(array)
        if array[i]>array[i+1]:
            #print(array)
            temp_gr=array[i]
            array[i]=array[i+1]
            array[i+1]=temp_gr
            simple_sort(array)
    return array



def main():
    #print(kombination([9,10,11,12,0]))
    print(prozentual_ausrechnen(1000000))
    #print(karten_ziehen(6))
    #print(simple_sort([11, 9, 10, 12, 0]))



if __name__ == "__main__":
    main()
