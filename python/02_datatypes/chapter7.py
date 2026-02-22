masala_spices = ("cardamom","cloves","cinamom")
(spice1,spice2,spice3) = masala_spices
print("Main masala spices ",spice1,spice2,spice3)
ginger_ratio,cardramom_ratio = (2,1)
print(f"Ratio is G:{ginger_ratio} and C:{cardramom_ratio} ")
# Swapping values
ginger_ratio,cardramom_ratio = cardramom_ratio,ginger_ratio
print(f" After swapping, Ratio is G:{ginger_ratio} and C:{cardramom_ratio}")

# Membership
print(f" Is ginger in masala spices? {'ginger' in masala_spices}")
print(f" Is cannamon in masala spices? {'cinamom' in masala_spices}")
