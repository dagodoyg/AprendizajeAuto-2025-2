import time

def timer(func):
    def wrapper(*args, **kwargs):
        init = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end-init)
        return result
    return wrapper

@timer
def sum(a: float, b: float): 
    return a+b

print(sum(1,2))
