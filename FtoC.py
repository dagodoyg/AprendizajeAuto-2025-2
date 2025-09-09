import math as m

def FtoC(tempF: float):
    tempC = (tempF - 32.0)*5.0/9.0
    print(f"{tempC:.1f}")
    return tempC

assert FtoC(0) 
