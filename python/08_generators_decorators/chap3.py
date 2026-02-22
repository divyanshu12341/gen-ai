# Send data to generators 
def chai_customer():
    print("What chai would you like?")
    order = yield
    while True: 
        print(f"Preparing {order}")
        order = yield

# Storing reference
stall = chai_customer()
# Starting generator
next(stall)

stall.send("Masala chai")
stall.send("Lemon chai")
