from functools import wraps


def log_activity(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Calling and {func.__name__}")
        result = func(*args,**kwargs)
        return result
    return wrapper

@log_activity
def brew_chai(type,milk = "no"):
    print(f" Brewing {type} chai and milk status {milk}")

brew_chai("masala chai")
