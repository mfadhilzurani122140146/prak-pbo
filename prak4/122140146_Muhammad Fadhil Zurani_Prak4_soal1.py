class Hewan:
    def __init__(self, nama, jenis_kelamin):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin

    def bersuara(self):
        pass

    def makan(self):
        print(f"{self.__class__.__name__} {self.nama} sedang makan: tulang")

    def minum(self):
        pass


class Kucing(Hewan):
    def bersuara(self):
        print(f"{self.__class__.__name__} {self.nama} bersuara: Meong!")
        super().bersuara()


class Anjing(Hewan):
    def bersuara(self):
        print(f"{self.__class__.__name__} {self.nama} bersuara: Guk Guk!")
        super().bersuara()


hewan1 = Kucing("Kiki", "Betina")
hewan2 = Anjing("Ichi", "Jantan")

print(hewan1.nama)  
print(hewan2.nama)  

hewan1.bersuara() 
hewan1.makan()     

hewan2.bersuara()  
hewan2.makan()   

