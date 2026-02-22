for token in range(1,11):
    print(f"Serving chai to token: #{token}")
for batch in range(1,5):
    print(f"Preparing for batch no: {batch}")
orders = ["Hitesh","Aman","Becky","Carlos"]
for name in orders:
    print(f" Order ready for {name} ")

menu = ["Green","Lemon","Spice","Mint"]
for index,val in list(enumerate(menu,start = 2)):
    print(f"Index is {index} and val is {val} ")


#Zip can combine lists
names = ["Divyanshu","Hitesh","Sam","Divyesh"]
bills = [50,70,100,55]
for names,bills in zip(names,bills):
    print(f"Name is {names} and bill is {bills} ")

# Walrus operator
value = 13
if (remainder := value % 5):
    print(f"Not divisible remainder is {remainder}")

available_sizes = ["small","medium","large"]
if(requested_size := input("Enter your chai cup size")) in available_sizes:
    print(f"Serving {requested_size} chai")
else:
    print(f"Size is unavailable - {requested_size}")

flavors = ["masala","ginger","lemon","mint"]
print(f"Available flavors {flavors} ")
while(flavor :=input("Enter flavor you want")) not in flavors:
    print(f"{flavor} you wrote is unavailable ")
print(f"You chose {flavor} for chai")

users = [
    {"id":1,"total":100,"coupon":"P20"},
    {"id":2,"total":150,"coupon":"F10"},
    {"id":3,"total":80,"coupon":"F50"}
]
discounts = {
    "P20":(0.2,0),
    "F10":(0.5,0),
    "P50":(0,10)
}

for user in users:
    percent,fixed = discounts.get(user["coupon"],(0,0))
    discount = user["total"]*percent + fixed 
    print(f"{user['id']} paid {user['total']} and got discount for next visit on {discount} ")
    
    