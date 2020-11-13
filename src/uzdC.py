### C. Temperatūras pārveidošana C->K
"""
    Funkcija akceptē vienu argumentu - temperatūru Celsija grādos,
    un atgriež temperatūru Kelvina grādos. Zemākā temperatūra
    Kelvina grādos var būt 0, tādēļ, ja aprēķinātā temperatūra ir
    zemāka, atgriež 0.

    Argumenti:
        t {int vai float} -- temperatūra Celsija grādos
    Atgriež:
        int vai float -- temperatūra Kelvina grādos
"""

def tmprtr(t) :
    k = t + 273.15
    if k <= 0 :
        k = 0
    return k
