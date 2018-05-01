#Projekt Dotyczący podaj mocne hasło

def bigLetter(passw):
    """Funkcja do sprawdzania czy jest duża litera w hasle"""
    for x in passw:
        if ord("x") >= 65 and ord("x") <= 90:
            return True
        return False

def specialChar(passw):
    """Funkcja do sprawdzania czy jest znak specjalny w hasle"""
    for x in passw:
        pass

def leng(passw):
    """Funkcja do sprawdzania czy haslo ma przynajmniej 8 znakow"""
    return len(passw) >= 8

def samePass(passw,passw2):
    """Funkcja dziala jesli podane hasla nie sa te same"""
    while passw != passw2:
        passw = input("Password incorrect, please try again: ")
        passw2 = input("Re-type password please: ")
    return passw,passw2

good = [None,None,None]

while good != [True,True,True]:
    passw = input("Give me password: ")
    passw2 = input("Re-type password please: ")

    if passw != passw2:
       passw,passw2 = samePass(passw,passw2)

    if leng(passw) == True:
        good[0] = True
    else:
        print("Password does not meet the requirement: Lenght")
        continue

    print(good)

print("Password Good")
        