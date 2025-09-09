import time

def decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return result
    return wrapper

@decorator
def sum(a: float, b: float) -> float:
    return a+b

print(sum(1,2))
