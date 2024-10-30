from szemelyauto import Szemelyauto
from teherauto import Teherauto
from autokolcsonzo import Autokolcsonzo
from berles import Berles

# Autókölcsönző létrehozása
kolcsonzo = Autokolcsonzo("Gyors Autókölcsönző")

# Autók hozzáadása
auto1 = Szemelyauto("ABC-123", "Toyota Yaris", 10000, 4)
auto2 = Szemelyauto("DEF-456", "Honda Civic", 12000, 4)
auto3 = Teherauto("GHI-789", "Ford Transit", 15000, 1000)

kolcsonzo.auto_hozzaadas(auto1)
kolcsonzo.auto_hozzaadas(auto2)
kolcsonzo.auto_hozzaadas(auto3)

# Bérlések létrehozása és hozzáadása
berles1 = Berles(auto1, 3)
berles2 = Berles(auto2, 2)
kolcsonzo.berles_hozzaadasa(berles1)
kolcsonzo.berles_hozzaadasa(berles2)

# Autók listázása
print("Autók listája:")
kolcsonzo.autok_listazasa()

# Bérlések listázása
print("\nBérlések listája:")
kolcsonzo.berlesek_listazasa()