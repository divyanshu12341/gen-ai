# ------------------------------------------------------------------
from ast import Nonlocal
from re import L


def print_order(name,chai_type):
    print(f"{name} ordered {chai_type}")

print_order("Aman","Masala")
print_order("Hitesh","Ginger")
print_order("Jia","Tulsi chai")

# --------------------------------------------------------------------------

def fetch_sales():
    print("Fetching sales data")

def filter_valid_sales():
    print("Filtering valid sales data")

def summarize_data():
    print("Summarizing sales data")

def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready")

generate_report()

def get_input():
    print("Getting user input")

def validate_input():
    print("Validating user info")

def save_to_db():
    print("Saving to DB")

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User registration complete")

register_user()

# --------------------------------------------------------------

def calculate_bill(cups,price_per_cup):
    return cups*price_per_cup

my_bill = calculate_bill(3,15)
print(my_bill)

# ----------------------------------------------------
def add_vat(price,vat_rate):
    return price*(100+vat_rate)/100

orders = [100,150,200]
for price in orders:
    final_amount = add_vat(price,10)
    print(f" Original : {price}, Final with vat: {final_amount}")

# -------------------------------------------------------------------
# SCOPES
def serve_chai():
    chai_type = "Masala"
    print(f"Inside function {chai_type} ")

chai_type = "Lemon"
serve_chai()
print(f"Outside function {chai_type}")

def chai_counter():
    chai_order = "Lemon" # Enclosing scope

    def print_order():
        chai_order = "Ginger"
        print(f"Inner {chai_order}")
    print_order()
    print(f"Outer {chai_order}")

chai_order = "Tulsi" #Global
chai_counter()

# -----------------------------------------------------------------------
def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update",chai_type)

update_order()

# --------------------------------------------------------------------------------------
chai_type = "Plain"
def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Irnai"
    kitchen()
front_desk()
print("Chai_type is ",chai_type)

# -------------------------------------------------------------------------------
chai = "Ginger chai"
def prepare_chai(order):
    print("Preparing ",chai)
prepare_chai(chai)

# ---------------------------------------------------------------------------------
# List is immutable
chai = [1,2,3]
def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai)


def make_chai(tea,milk,sugar):
    print("Tea is ",tea)
    print("Milk is ",milk)
    print("Sugar is ",sugar)

make_chai("Darjleeing","Yes","Low")
make_chai(sugar = 'Med',tea = 'Prakrati',milk = 'Yes')

# arg  --> arguments
# kwarg --> key value args
def special_chai(*ingredients,**extras):
    print("Ingredients: ",ingredients)
    print("Extras: ",extras)

special_chai('Cinnamon','Cardamom',sweetener='Honey',foam='Yes')

def chai_orders(order = []):
    order.append('Masala chai')
    print("Order: ",order)

chai_orders()

def chai_ordersss(order = None):
    if order is None:
        order = []
    print(order)

chai_ordersss()

# ------------------------------------------------------------------
# Handle multiple returns in python
# Nothing --> implicitly returns None
# We can return either one value or multiple values from a function
def make_chai():
    return "Here is your masala chai"

return_value = make_chai()
print(return_value)


# implicitly returns None when returning nothing
def idle_chaiwala():
    pass
print(idle_chaiwala())

# returns one value
def sold_cups():
    return 120
print(sold_cups())

# returns early from a function
# if function hits return other code doesn't get executed
def chai_status(cups_left):
    if cups_left == 0:
        return "sorry,chai over"
    return "chai is ready"

chai_left = chai_status(0)
print(chai_left)
chai_ready = chai_status(10)
print(chai_ready)

def chai_report():
    return 20,100
print(chai_report())

sold,remaining = chai_report()
print("No of chai sold is ",sold)
print("No of chai remaining is ",remaining)

def chai_report2():
    return 100,20,10

sold,remaining,_ = chai_report2()
print("Sold is ",sold)
print("Remaining is ",remaining)

# ---------------TYPES OF FUNCTIONS -------------------------
# PURE VS IMPURE
# RECURSIVE FUNCTIONS
# ANONYMOUS FUNCTIONS/LAMBDAS FUNCTIONS

# Pure function doesn't manipulate any value globally
def pure_chai(cups):
    return cups*10

pureChai = pure_chai(6)
print(pureChai)

# Impure function manipulate values globally

# Not recommended
total_chai = 0
def impure_chai(cups):
    global total_chai
    total_chai += cups

impure_chai(total_chai)


# Recursive function
def pour_chai(n):
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

pourChai = pour_chai(3)
print(pourChai)

# Lambdas functions
chai_types = ["light","kadak","ginger","kadak"]
strong_chai = list(filter(lambda chai: chai == "kadak",chai_types))
print(strong_chai)

# -----------------------------------------------------
# Built in functions 

def chai_flavor(flavor = "masala"):
    """Return the  flavor of chai"""
    return flavor

# It should be exactly first line 
print(chai_flavor.__doc__)
print(chai_flavor.__name__)

help(len)

def chai_bill(chai = 0,samosa=0):
    """
    Calculate total bill for chai and samosa 
    : param chai: No of chai cups(10 rupees each)
    : param samosa: No of samosas(15 rupees each)
    : return: (total amount,thank you message)
    """
    total = chai*10 + samosa*15
    return total,"Thanks for ordering chai and samosa"


chaiBill = chai_bill(10,11)
print(chaiBill)
print(chai_bill.__doc__)
