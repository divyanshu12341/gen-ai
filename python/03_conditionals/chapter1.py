kettle_boiled = True
if kettle_boiled:
    print("Time to make some chai ")

user_input = input("Enter snack you want? ").lower()
print(user_input)
if user_input == "cookies" or user_input == "samosa":
    print("Confirm order")
else:
    print("Unavailable")

cup = input("Choose your cup size(small/medium/large): ").lower()
if cup=="small":
    print("Price is 10rs")
elif cup=="medium":
    print("Price is 15rs")
elif cup=="large":
    print("Price is 20rs")
else:
    print("Invalid cup size")

device_status = "active"
temperature = 36
if device_status == "active" and temperature>35:
    print("High temperature")
elif device_status == "active":
    print("Normal temperature")
elif device_status == "off":
    print("Device is offline ")

order_amount = input("Enter order amount")
order_amount = int(order_amount)
delivery_fee = 0 if order_amount>300 else 30
print(delivery_fee)

seat_type = input("Enter seat type(Sleeper/AC/General/Luxury)").lower()
match seat_type:
    case "sleeper":
        print("Sleeper has no AC but beds are available")
    case "ac":
        print("AC has both beds and Air conditioned but costlier than sleeper")
    case "general":
        print("Cheapest option available")
    case "luxury":
        print(" Premium seats with meals")
    case _:
        print("Invalid seat type")
