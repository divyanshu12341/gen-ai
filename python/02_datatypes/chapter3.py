# Integer
black_tea_grams = 14
ginger_grams = 3

total_grams  = black_tea_grams + ginger_grams
print(f" Total grams of base tea is {total_grams}")
remaining_tea = total_grams-ginger_grams
print(f" Total grams of remaining tea is {remaining_tea}")

milk_litres = 7
servings = 4
milk_per_serving = milk_litres/servings
print(f"Milk per serving is {milk_per_serving}")

total_tea_bags = 7
pots = 4
# // means it doesn't care about decimals
bags_per_pot = total_tea_bags // pots
print(f"Bags per pot is {bags_per_pot}")

total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup
print(f"Leftover pods is {leftover_pods}")

base_flavor_strength = 2
scale_factor = 3
powerful_flavor = base_flavor_strength ** scale_factor
print(f" Scaled flavor strength: {powerful_flavor}")

total_tea_leaves_harvested = 1_000_000_0000
print(total_tea_leaves_harvested)

