class A:
    label = "A: Simple base class"

class B(A):
   label = "B: Masala blend"

class C(A):
   label = "C: Purple blend"

class D(B,C):
    pass

cup = D
print(cup.label)
