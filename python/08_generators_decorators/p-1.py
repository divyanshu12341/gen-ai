import time


def timing(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(f"{func.__name__} took {time.time() - start:2f}s")
        return result
    return wrapper

@timing
def slow_func():
    print("Now timed")

slow_func()

def log_calls(func):
    def wrapper(*args,**kwargs):
        print(f"Calling {func.__name__}")
        return func(*args,**kwargs)
    return wrapper

@log_calls
def add(a,b):
    return a+b

add(3,5)

def validate_positive(func):
    def wrapper(x):
        if x<=0:
            raise ValueError("Value must be less than 0")
        return func(x)
    return wrapper

@validate_positive
def sqrt(x):
    return x**0.5

sqrt(32)    

