# ### D. Temperatūras pārveidošana F->C

#     Funkcija akceptē vienu argumentu - temperatūru Fārenheita grādos,
#     un atgriež temperatūru Celsija grādos. Zemākā temperatūra
#     Celsija grādos var būt −273.15, tādēļ, ja aprēķinātā temperatūra ir zemāka, 
#     atgriež −273.15.

#     Argumenti:
#         t {int vai float} -- temperatūra Fārenheita grādos
#     Atgriež:
#         int vai float -- temperatūra Celsija grādos

# °C = (°F − 32) / 1,8

import pytest
from src.uzdD import temp

def test_uzdD_rez_0():
     assert temp(32) == 0

def test_uzdD_273_15():
     assert temp(-459.67) == pytest.approx(-273.15)

def test_uzdD_parak_mazs_mazaks_par_rez_273_15():
     assert temp(-460) == pytest.approx(-273.15)

def test_uzdD_int():
     assert temp(300) == pytest.approx(148.88889)