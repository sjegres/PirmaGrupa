# ### A. Drošs dalījums

#     Funkcija akceptē divus argumentus - skaiļus a un b,
#     aprēķina to dalījumu un atgriež to. Ja skaiļus dalīt nedrīkst,
#     atgriež 0.

#     Argumenti:
#         a {int vai float} -- pirmais skaitlis
#         b {int vai float} -- otrais skaitlis
#     Atgriež:
#         int vai float -- rezultāts

def dross_dalijums(a, b):
    if b != 0:
        return a / b
    else:
        return 0

print(dross_dalijums(2, 3))
print(dross_dalijums(-32, 6))
print(dross_dalijums(0.345, 5.34))
