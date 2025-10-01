import random

def ziehung():
    zahlen = []
    for i in range(1, 46):
        zahlen.append(i)
    for i in range(0, 6):
        zahl = random.randint(1, 45-i)
        gezogeneZahl=zahlen[zahl-1]
        zahlen[zahl-1] = zahlen[len(zahlen)-i-1]
        zahlen[len(zahlen)-i-1] = gezogeneZahl #=zahl geht nicht weil sonst die schon veränderte Zahl verloren gehen würde
    #print(zahlen)
    return zahlen


auswertung ={}
for i in range(1, 46):
    auswertung[i] = 0
for i in range(1, 1001):
    aktuelleZiehung = ziehung()
    for j in range(0, 6):
        auswertung[aktuelleZiehung[len(aktuelleZiehung)-1-j]] += 1
print(auswertung)

#einfacher ohne Shuffel in der Liste dafür mit Abfrage
#Logik leichter zu verstehen
"""
def sechsZufallszahlen():
    durchgaenge=0
    verwendeteZahlen =[]

    while durchgaenge<6:
        zufallszahl = random.randint(1, 45)
        if zufallszahl not in verwendeteZahlen:
                #print(zufallszahl)
                verwendeteZahlen.append(zufallszahl)
                durchgaenge=durchgaenge+1
    return verwendeteZahlen

auswertung ={}
for i in range(1, 46):
    auswertung[i] = 0
for i in range(1, 1001):
    aktuelleZiehung = sechsZufallszahlen()
    for j in range(0, 6):
        aktuelleZiehung[j]
        auswertung[aktuelleZiehung[j]] += 1
print(auswertung)

"""