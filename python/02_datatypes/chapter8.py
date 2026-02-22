# Memory reference cannot be changed

ingredients = ["water","milk","black tea"]
ingredients.append("sugar")
print(f"Ingredients are {ingredients}")
ingredients.remove("water")
print(f"Ingredients are {ingredients}")
spice_options = ["ginger","cardamom"]
chai_ingredients = ["water","milk"]
chai_ingredients.extend(spice_options)
print(chai_ingredients)
chai_ingredients.insert(2,"Green Tea")
print(chai_ingredients)

last_added = chai_ingredients.pop()
print("Element removed ",last_added)
chai_ingredients.reverse()
print(chai_ingredients)
chai_ingredients.sort()
print(chai_ingredients)
sugar_levels = [1,2,3,4,5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

base_liquid = ["water","milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(full_liquid_mix)

# 3 times black tea will be added
strong_brew = ["black tea"]*3
print(strong_brew)

# It maintains order
strong_brew = ["black tea","water"]*3
print(strong_brew)

raw_spice_data = bytearray(b"CINNAMMOON")
print(f"Bytes: {raw_spice_data}")


raw_spice_data = raw_spice_data.replace(b"CINNA",b"CARDI")
print(raw_spice_data)
