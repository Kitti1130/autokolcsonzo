class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def auto_hozzaadas(self, auto):
        self.autok.append(auto)

    def autok_listazasa(self):
        for auto in self.autok:
            print(auto.get_info())

    def berles_hozzaadasa(self, berles):
        self.berlesek.append(berles)

    def berlesek_listazasa(self):
        for berles in self.berlesek:
            print(berles.get_info())