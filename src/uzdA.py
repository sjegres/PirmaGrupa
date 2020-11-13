def temp(f):
    gradi = (f - 32) * 5/9
    if gradi < -273.15:
        gradi = -273.15
    return gradi