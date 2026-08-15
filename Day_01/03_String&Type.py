a="h"
print(ord(a))

b="H"
print(ord(b))


ord("A")   # → 65  (Unicode of A)
chr(65)   # → "A" (Character from Unicode)



# String Indexing
a = "Hello"
#   H  e  l  l  o
#   0  1  2  3  4   ← positive
#  -5 -4 -3 -2 -1   ← negative

print(a[0])   # H
print(a[-1])  # o



# String Slicing
a = "hello"
print(a[1:4])    # ell  (index 1,2,3 — 4 excluded)
print(a[::-1])   # olleh  (reversed!)



a=10
b=str(a)

print(type(b))