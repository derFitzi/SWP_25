import string

# Buchstaben aus gemischten String herausholen
def listComprehension(zahlenWortMix):
    return[zeichen for zeichen in zahlenWortMix if zeichen.isalpha()]

# Mit welchen verschiedenen Buchstaben fangen Wörter in einem Satz an?
def setComprehension(satz):
    return {wort[0] for wort in satz.split()} # ist case sensitive wort.lower()[0]

# Gibt aus, ob eine Zahl gerade oder ungerade ist
def dictComprehension(bis):
    return{zahl+1:"ungerade" if (zahl+1)%2 else "gerade" for zahl in range(bis)}

"""
def dictComprehensionAlphabet(alphabet):
    return{buchstabe: ord(buchstabe)-64 for buchstabe in alphabet}
"""
# Wandelt ein geordnetes Alphabet als String in ein Dictionary mit "Index" aus, erster Buchstabe hat immer Index 1
def dictComprehensionAlphabet(alphabet):
    return{buchstabe: ord(buchstabe)-(ord(alphabet[0])-1) for buchstabe in alphabet}

def main():
    print("List Comprehension: ", listComprehension("12h2343a23ll983475o3459082345"))
    print("Set Comprehension: ", setComprehension("Ich bin ein Satz mit vielen Wörtern und einigen Wiederholungen"))
    print("Dict Comprehension: ", dictComprehension(10))

    print(dictComprehensionAlphabet("ABCDEFGHIJKLMNOPQRATUVWXYZ"))
    print(dictComprehensionAlphabet(string.ascii_uppercase))    # nicht Hardcoded
    teilweise_alphabet = ''.join([buchstabe for buchstabe in string.ascii_uppercase][6:24])  # Liste aus String, diese slicen und dann zu String joinen
    print(dictComprehensionAlphabet(teilweise_alphabet))

if __name__ == "__main__":
    main()
