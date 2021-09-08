# Tuple
t = (1, 2, 3)
print(t)

t = 1, 2, 3
print(t)

t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')
t3 = t1+t2
print(t3)
print(t1*3)

print((123,))  # single value tuple
print(())

x, y = (1, 2)
print(x)
print(y)


def min_max(ls):
    min_value = min(ls)
    max_value = max(ls)
    return min_value, max_value


z = min_max([1, 2, 3, 4])
print(z)

# Swap
x = 2
y = 3
y, x = x, y
print(x)
print(y)

print(1 in t1)
print(5 in t)
print(1 not in t1)
print(5 not in t1)
