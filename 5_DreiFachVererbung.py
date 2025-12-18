class Trashbin:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume

class Automated_trashbin(Trashbin):
    def __init__(self, color, volume, trash_sorts):
        super().__init__(color, volume)
        self.trash_sorts = trash_sorts

class Super_coole_ki_gestuetzte_Diplomarbeit_namens_Smart_Trash_bin(Automated_trashbin):
    def __init__(self, color, volume, trash_sorts,sortingspeed):
        super().__init__(color, volume, trash_sorts)
        self.sortingspeed = sortingspeed

    def __str__(self):
        pass

def main():
    diplomarbeit = Super_coole_ki_gestuetzte_Diplomarbeit_namens_Smart_Trash_bin("grey",100,["paper", "plastic", "residual waste"], 20)
    print(diplomarbeit.trash_sorts)

if __name__ == '__main__':
    main()
