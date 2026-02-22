# Generators --> we save memory
# don't want results immediately
# lazy evaluation
def serve_chai():
    yield "Cup 1: Masala chai"
    yield "Cup 2: Ginger chai"
    yield "Cup 3: Elaichi chai"

stall = serve_chai()

for cup in stall:
    print(cup)

def get_chai_list():
    return ["Cup 1","Cup 2","Cup 3"]

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

# It just holds reference of a function not function values itself
chai = get_chai_gen()
print(chai)
# function get paused after yielding first value 
print(next(chai))
print(next(chai))
