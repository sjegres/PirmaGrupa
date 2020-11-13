import pytest
from src.uzdB import summa

def avienads0():
    assert (0, 5) == 0

def bvienads0() 
    assert (5, 0) == 0

def aminus1() 
    assert (-1, 3) == 0

def bminus1() 
    assert (3, -1) == 0

def normal() 
    assert (4, 5) == 10    

"""
### B. Trijstūra laukums

    Funkcija akceptē divus argumentus - trisjtūra augstumu un pamatu,
    aprēķina trijstūra laukumu un atgriež to. Ja kāds no argumentiem ir mazāks vai vienāds ar 0, atgriež 0.
    Formula trijstūra laukuma aprēķināšanai ir augstums*pamats/2

    Argumenti:
        h {int vai float} -- trijstūra augstums
        p {int vai float} -- trijstūra pamats
    Atgriež:
        int vai float -- rezultāts
"""