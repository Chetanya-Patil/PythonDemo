x = int("1")
y = int(1)
z = int("abc")
print(type(z))  # it will show error becoz literals we used is not able to convert that to int.

p = 1
p = float(p)
print(p)
print(type(p))

q = 1.0
q = int(q)
r = str(q)
print(q)
print(type(q))

print(type(r))