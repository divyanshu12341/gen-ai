from cProfile import label

chai_type = "Ginger Chai"
customer_name = "Priya"
print(f" Order for {customer_name}: {chai_type} please !")

# last number is not inclusive in case of python
# Here index starts from 0
chai_description = "Aromatic and Bold"
print(f"First letter: {chai_description[0]}")
print(f"First word: {chai_description[0:8]}")
print(f"First word with alternate characters: {chai_description[0:8:2]}")
# s[start:stop:step]
# s[: :-1] --> -1 is shorthand for reversing whole string
print(f"Last word: {chai_description[12:]}")

label_text = "Chai Sp'ecial"
encoded_label = label_text.encode("UTF-8")
print(f"Encoded label for text : {encoded_label}")
print(f"Non encoded label : {label_text}")
decoded_label = encoded_label.decode("UTF-8")
print(f" Decoded label: {decoded_label}")
