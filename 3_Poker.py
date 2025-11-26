import random
import unittest
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
"""
#Ursprüngliche Funktion
def pair(farben, werte):
    if (len(set(werte))<len(werte)):
        return True
    return False
"""
def pair(farben, werte):
    return (False, True)[len(set(werte))<len(werte)] # ternärer Operator mit tuple für Übung

"""
#Ursprüngliche Funktion
def two_pair(farben, werte):
    if (len(set(werte))<=len(werte)-2):
        return True
    return False
"""
def two_pair(farben, werte):
    return {True: 1, False: 0}[len(set(werte))<=len(werte)-2] # ternärer Operator mit dict für Übung

def triplett(farben, werte):
    werte=simple_sort(werte)
    if (len(set(werte))<=len(werte)-2):
        if (werte[0] == werte[1] == werte[2]) or (werte[2] == werte[3] == werte[4]) or (werte[1]==werte[2]==werte[3]):
            return True
    return False

def straight(farben, werte):
    werte = sorted(set(werte))
    if len(werte) != 5:
        return False
    if werte[-1] - werte[0] == 4:
        return True
    if set(werte) == {0, 1, 2, 3, 4}:
        return True
    if set(werte) == {0, 9, 10, 11, 12}:
        return True
    return False


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
    werte = sorted(werte)
    if werte[0] == werte[1] == werte[2] == werte[3]:
        return True
    if werte[1] == werte[2] == werte[3] == werte[4]:
        return True
    return False


def straight_flush(farben, werte):
    return flush(farben, werte) and straight(farben, werte)

def royal_flush(farben, werte):
    return flush(farben, werte) and set(werte) == {0,9,10,11,12}


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
    print("Absolute Ergebnisse: ",absolute_zahlen)
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

def fehler_berechnen(prozentuale_auswertung, rechenwerte):
    for i in range(len(prozentuale_auswertung)):
        prozentuale_auswertung[i]=(prozentuale_auswertung[i]/rechenwerte[i]*100)-100
    return prozentuale_auswertung




def main():
    richtige_werte={0:50.1177, 1:42.2569,2:4.7539,3:2.1128,4:0.3925,5:0.1965,6:0.1441,7:0.024,8:0.00139, 9:0.000154 }
    #print(kombination([9,10,11,12,0]))
    #print(prozentual_ausrechnen(1000000))
    #print(karten_ziehen(6))
    #print(simple_sort([11, 9, 10, 12, 0]))
    prozente = prozentual_ausrechnen(1000000)
    print("Prozentuale Ergebnisse: ",prozente)
    print("Prozentuale Abweichungen: ",fehler_berechnen(prozente,richtige_werte))

class Test_Pair(unittest.TestCase):
    def test_NormalCase(self):
            farben = [0, 1, 2, 3]
            werte = [5, 7, 9, 5]
            self.assertTrue(pair(farben, werte), "Pair nicht erkannt")
    def test_NoPair(self):
            farben = [0, 1, 2, 3, 0]
            werte = [5, 7, 9, 11, 13]
            self.assertFalse(pair(farben, werte), "Falsches Pair erkannt")
    def test_EdgeCase(self):
            farben = [0, 0]
            werte = [5, 5]
            self.assertTrue(pair(farben, werte), "Pair nicht erkannt im Edge Case")

class Test_FehlerBerechnen(unittest.TestCase):
    def test_NormalCase(self):
            prozentuale_auswertung = {0: 50.0, 1: 40.0, 2: 5.0}
            rechenwerte = {0: 50.0, 1: 42.0, 2: 4.0}
            self.assertEqual(fehler_berechnen(prozentuale_auswertung, rechenwerte), {0: 0.0, 1: -4.761904761904773, 2: 25.0}, "Fehlerberechnung falsch")
    def test_DivideByZero(self):
            prozentuale_auswertung = {0: 50.0}
            rechenwerte = {0: 0.0}
            with self.assertRaises(ZeroDivisionError):
                fehler_berechnen(prozentuale_auswertung, rechenwerte)
    def test_NoInput(self):
            prozentuale_auswertung = {}
            rechenwerte = {}
            self.assertEqual(fehler_berechnen(prozentuale_auswertung, rechenwerte), {}, "Fehler für leere Eingabe falsch")

class Test_SimpleSort(unittest.TestCase):
    def test_NormalCase(self):
            array = [5, 3, 8, 1, 2]
            self.assertEqual(simple_sort(array), [1, 2, 3, 5, 8], "Falsch sortiert")
    def test_AlreadySorted(self):
            array = [1, 2, 3, 4, 5]
            self.assertEqual(simple_sort(array), [1, 2, 3, 4, 5], "Schon Sortiertes Array wurde verändert")
    def test_EmptyArray(self):
            array = []
            self.assertEqual(simple_sort(array), [], "Leeres Array falsch behandelt")

if __name__ == "__main__":
    main()
    #unittest.main() #Test müssen über dem Main sein sonst werden sie nicht gefunden





