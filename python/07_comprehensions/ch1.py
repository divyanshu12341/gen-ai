# Comprehensions are used to
# 1) filter item
# 2) transform item
# 3) create a new collection
# 4) flatten a nested structure

# What purpose comprehensions serve:
# 1) cleaner code
# 2) Faster execution


# Types of comprehensions:
# 1) List
# 2) Set
# 3) Dictionary
# 4) Generator

# --------------------LIST COMPREHENSIONS --------------------------
menu = [
    "Masala chai",
    "Iced Lemon Tea",
    "Green tea",
    "Iced peach tea",
    "Ginger chai"
]
#  [expression for item in iterable if condition ] --> comprehensions 
iced_tea = [tea for tea in menu if "Iced" in tea]
print(iced_tea)

# ----------------------SET COMPREHENSIONS --------------------------
