class Chai:
    # variables --> properties
    origin = "India"

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

# Creating objects from class chai
# Each object has it's own namespace 
masala = Chai()
print(f"Masala:{masala.origin} ")
print(f"Masala: {masala.is_hot} ")
masala.is_hot = False
print(f"Masala: {masala.is_hot}")
print(f"{Chai.is_hot}")
