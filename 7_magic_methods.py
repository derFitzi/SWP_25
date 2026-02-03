"""
- Magic methods

- len(a) = a.__len__()

- Auto Klasse erzeugen
- PS als attribut vergeben
- wenn a1 50PS hat und a2 60PS und a1+a2 rechnet soll direkt 110 ausgegeben werden
- subtraktion und multiplikation soll auf den auto-objekten möglich sein
- achtung überprüfen ob geegnete objekte addiert, subtrahiert usw. werden
- EQ,LT,GT vergleichsoperationen abbilden
- für alle magicmethods testzeilen angeben



später bei linkedlist:

 __setitem__ __getitem__ __contains__=in operator

with = contextmanager klappt, wenn eine klasse __enter_ und __exit implementiert

iteratoren müssen __iter__ __next__ implementiert next braucht raise Stopiteration
"""

class auto:
    def __init__(self, ps):
        self.ps = ps
        if not isinstance(ps, int) or ps < 0:
            raise ValueError("PS muss eine positive ganze Zahl sein")

    def __add__ (self, other):
        if isinstance(other, auto):
            return self.ps + other.ps
        if isinstance(other, int):
            return self.ps + other
        raise TypeError("Objekt ist weder Auto noch PS Zahl") # NotImplemented anscheinend geeigneter



    def __sub__ (self, other):
        if isinstance(other, auto):
            return self.ps - other.ps
        if isinstance(other, int):
            return self.ps - other
        raise TypeError("Objekt ist weder Auto noch PS Zahl")

    def __mul__(self, other):
        if isinstance(other, auto):
            return self.ps * other.ps
        if isinstance(other, int):
            return self.ps * other
        raise TypeError("Objekt ist weder Auto noch PS Zahl")

    def __eq__ (self, other):
        if isinstance(other, auto):
            return self.ps == other.ps
        if isinstance(other, int):
            return self.ps == other
        raise TypeError("Objekt ist weder Auto noch PS Zahl")

    def __lt__ (self, other):
        if isinstance(other, auto):
            return self.ps < other.ps
        if isinstance(other, int):
            return self.ps < other
        raise TypeError("Objekt ist weder Auto noch PS Zahl")

    def __gt__ (self, other):
        if isinstance(other, auto):
            return self.ps > other.ps
        if isinstance(other, int):
            return self.ps > other
        raise TypeError("Objekt ist weder Auto noch PS Zahl")

    # Reverse Operations wären mit dem gleichen nur gedreht (other, self) für print(50+Ferrari)

    def __str__(self):
        return str(self.ps)

def main():
    Ferrari = auto(800)
    Fiat = auto(50)
    Ford = auto(150)
    Madzda = auto(140)
    Audi = auto(150)

    print("Alle PS Zahlen:")
    print(Ferrari, Fiat, Ford, Madzda, Audi)

    print("Addieren:")
    print(Ferrari + Fiat)

    print("Subtrahieren:")
    print(Ford - Madzda)

    print("Multiplizieren:")
    print(Ferrari * Fiat)

    print("Größer als: ")
    print(Ford > Madzda)

    print("Kleiner als")
    print(Ferrari < Ford)

    print("Verkettung mit mehreren:")
    print(Ferrari + (Madzda*Fiat)) # Verkettung durch Erlauben das other Zahl sein darf

    print("Gleich: ")
    print(Ford == Audi)

    print("Fehler: ")
    #print(Ford + "G")
    BMW = auto(-10)



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Fehler aufgetreten:", e)
