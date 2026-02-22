# Create a list of squares for only even no between 1 and 20
squares = [sq for sq in range(1,21) if sq%2==0]
print(squares)
# Given a list of names, create a new list containing only the
#  names that start with "S".
names = ["Steve", "Alice", "Sarah", "Bob", "Sam", "Quincy"]
nameStartWithS = [val for val in names if val[0]=="S"]
print(nameStartWithS)

# Convert a list of temperatures in Celsius to Fahrenheit.
celsius = [0, 10, 20, 25, 30, 38]
farenheit = [val*1.8+32 for val in celsius]
print(farenheit)
# Replace negative numbers in a list with 0,
# keeping positive numbers as they are.

# x if condition else for y in x
numbers = [10, -5, 3, -1, 0, 7, -8]
posNum = [0 if num<0 else num for num in numbers]
print(posNum)

# 
sentence = "Generative Artificial Intelligence is transforming the world"
senMap = [sen[sen.index(' ')-1] for sen in sentence if sen == " "]
print(senMap)
