def sum(a: float, b: float) -> float:
    """Returns the sum of a and b"""
    return a + b

print(sum(1,2))
try:
    print(sum(a,b))
except:
    print("bad input")
