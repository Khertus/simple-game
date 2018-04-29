#Projekt Dotyczący podaj mocne hasło

def bigLetter(passw):
    """Funkcja do sprawdzania czy jest duża litera w hasle"""
    pass

def specialchar(passw):
    """Funkcja do sprawdzania czy jest znak specjalny w hasle"""
    pass

def leng(passw):
    """Funkcja do sprawdzania czy haslo ma przynajmniej 8 znakow"""
    return len(passw >= 8)

good = None

while good != True:
    passw = input("Give me password: ")
    passw2 = input("Re-type password please: ")
