# Buchstaben aus gemischten String herausholen
def listComprehension(zahlenWortMix):
    return[zeichen for zeichen in zahlenWortMix if zeichen.isalpha()]

# Mit welchen verschiedenen Buchstaben fangen Wörter in einem Satz an?
def setComprehension(satz):
    return {wort[0] for wort in satz.split()} # ist case sensitive wort.lower()[0]

# Gibt aus, ob eine Zahl gerade oder ungerade ist
def dictComprehension(bis):
    return{zahl:"ungerade" if (zahl%2) else "gerade" for zahl in range(bis)}


def main():
    print("List Comprehension: ", listComprehension("12h2343a23ll983475o3459082345"))
    print("Set Comprehension: ", setComprehension("Ich bin ein Satz mit vielen Wörtern und einigen Wiederholungen"))
    print("Dict Comprehension: ", dictComprehension(10))

if __name__ == "__main__":
    main()
