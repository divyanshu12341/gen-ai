# Generators are used for saving the memory
# (expression for item in iterable if condition)

daily_sales = [5,10,12,7,3,8,9,15]
# It is memory efficient operation 
total_cups = sum(sales for sales in daily_sales if sales>5)
print(total_cups)

