class Chaicup:
    size = 150 
    
    def describe(self):
        return f"A {self.size}ml chai cup"
    
cup = Chaicup()
print(cup.describe())

cup_two = Chaicup()
cup_two.size = 100
print(cup_two.describe())
print(Chaicup.describe(cup_two))
