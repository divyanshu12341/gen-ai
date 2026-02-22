# Attribute shadowing
class Chai:
    temperature = "Hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
print("After changing ",cutting.temperature)
print("Direct looking at class ",Chai.temperature)

# if object attribute deleted then it fallbacks to class one 
del cutting.temperature
print(cutting.temperature)

