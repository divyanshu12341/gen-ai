# Set comprehension
# {expression for item in iterable if condition}
favourite_chais = ["Masala chai","Green tea","Masala chai","Lemon tea","Green tea","Elaichi tea"]
unique_chai = {chai for chai in favourite_chais}
print(unique_chai)

recipes = {
    "Masala chai":["Ginger","Cardamom","Clove"],
    "Elaichi chai":["cardamom","milk"],
    "Spicy chai":["Ginger","Black pepper","clove"]
}

unique_spices = {
    spice for ingredients in recipes.values() for spice in ingredients
}
print(unique_spices)

