x = 5000
print(id(x))
y = x
print(id(y))

z = 5000

w = 500
print(x is y)
print(x is z)
print(x is w)
t = None
print(t is None)
print(id(t))

l1 = [1,2,3]
l2 = [1,2,3]
print(id(l1))
print(id(l2))

print(l1 is l2)
print (l1 ==l2)