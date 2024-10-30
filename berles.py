class Berles:
    def __init__(self, auto, napok_szama):
        self.auto = auto
        self.napok_szama = napok_szama

    def get_info(self):
        osszeg = self.auto.berleti_dij * self.napok_szama
        return f"Bérelt autó: {self.auto.rendszam}, Napok száma: {self.napok_szama}, Összeg: {osszeg} Ft"