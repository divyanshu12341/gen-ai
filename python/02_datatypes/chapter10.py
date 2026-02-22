from calendar import c

chai_order = dict(type = "Masala chai",size = "Large",sugar = 2)
print(chai_order)

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"
print(f"Recipe base: {chai_recipe}")
del chai_recipe["liquid"]
print(f"{chai_recipe}")
print(f" Is sugar in chai order? {'sugar' in chai_order}")
chai_order = {"type":"Ginger chai","size":"medium","sugar":1}
print(f"Order details (keys): {chai_order.keys()}")
print(f"Order details (values): {chai_order.values()}")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item} ")

extra_spices = {
    "cardamom":"crushed",
    "ginger":"slices"
}
chai_recipe.update(extra_spices)
print(chai_recipe)

customer_note = chai_order.get("note","NO NOTE")
print(customer_note)
