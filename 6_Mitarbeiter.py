class Person:
    def __init__(self, name, geschlecht):
        self.name = name
        if geschlecht.lower() not in ('m', 'w'):
            raise ValueError("Geschlecht muss 'm' oder 'w' sein")
        self.geschlecht = geschlecht.lower()

class Mitarbeiter(Person):
    def __init__(self, name, geschlecht, abteilung):
        super().__init__(name, geschlecht)
        self.abteilung = abteilung
        self.abteilung.add_mitarbeiter(self)

class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, geschlecht, abteilung):
        super().__init__(name, geschlecht, abteilung)
        abteilung.set_leiter(self)

class Abteilung:
    def __init__(self, name):
        self.name = name
        self.mitarbeiter = []
        self.leiter = None

    def add_mitarbeiter(self, mitarbeiter):
        if mitarbeiter not in self.mitarbeiter:
            self.mitarbeiter.append(mitarbeiter)

    def set_leiter(self, leiter):
        if self.leiter is not None:
            raise ValueError(f"{self.name} hat bereits einen Leiter")
        self.leiter = leiter

    def mitarbeiterzahl(self):
        return len(self.mitarbeiter)

class Firma:
    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def add_abteilung(self, abteilung):
        if abteilung not in self.abteilungen:
            self.abteilungen.append(abteilung)

    def anzahl_mitarbeiter(self):
        return sum(len(ab.mitarbeiter) for ab in self.abteilungen)

    def anzahl_abteilungsleiter(self):
        return sum(1 for ab in self.abteilungen if ab.leiter is not None)

    def anzahl_abteilungen(self):
        return len(self.abteilungen)

    def abteilung_mit_groesster_mitarbeiterzahl(self):
        if not self.abteilungen:
            return None
        return max(self.abteilungen, key=lambda ab: ab.mitarbeiterzahl())

    def prozentanteil_geschlechter(self):
        gesamt = 0
        maennlich = 0
        weiblich = 0
        for ab in self.abteilungen:
            for m in ab.mitarbeiter:
                gesamt += 1
                if m.geschlecht == 'm':
                    maennlich += 1
                else:
                    weiblich += 1
        if gesamt == 0:
            return {'m': 0, 'w': 0}
        return {'m': maennlich / gesamt * 100, 'w': weiblich / gesamt * 100}


if __name__ == "__main__":
    firma = Firma("TechSolutions")

    it = Abteilung("IT")
    vertrieb = Abteilung("Vertrieb")
    hr = Abteilung("HR")

    firma.add_abteilung(it)
    firma.add_abteilung(vertrieb)
    firma.add_abteilung(hr)

    Abteilungsleiter("Achi", "m", it)
    Mitarbeiter("Baumann", "m", it)
    Mitarbeiter("Egger", "w", it)

    Abteilungsleiter("Lukas", "m", vertrieb)
    Mitarbeiter("Sabine", "w", vertrieb)
    Mitarbeiter("Tom", "m", vertrieb)
    Mitarbeiter("Julia", "w", vertrieb)

    Abteilungsleiter("Marc", "w", hr)
    Mitarbeiter("Stefan", "m", hr)

    print(f"Anzahl Mitarbeiter: {firma.anzahl_mitarbeiter()}")
    print(f"Anzahl Abteilungsleiter: {firma.anzahl_abteilungsleiter()}")
    print(f"Anzahl Abteilungen: {firma.anzahl_abteilungen()}")
    größte_abteilung = firma.abteilung_mit_groesster_mitarbeiterzahl()
    print(f"Abteilung mit den meisten Mitarbeitern: {größte_abteilung.name}")
    geschlechter = firma.prozentanteil_geschlechter()
    print(f"Prozent Männer: {geschlechter['m']:.1f}%, Frauen: {geschlechter['w']:.1f}%")
