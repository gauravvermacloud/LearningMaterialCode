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

print(tuple([1, 2, 3]))
print(tuple("Hello"))

############## Strings #####################
s = "Hello world"
print(len(s))

print(' - '.join(["Hello", "world", "27"]))

print("Hello world there".split(" "))

print("This is {0} string being formatted with {1} and {0}".format(
    "This", 7
))

print("""This is {First} string being formatted with name values 
      {Second} and {First}""".format(
    First="This", Second=7
))


############# range ######################

x = range(5)
print(x)

for i in x:
    print(i)

l = list(range(2, 10, 3))
print(l)

l = list(range(10, 2, -2))
print(l)

c = [1, 2, 3, 4, 5]

for i in enumerate(c):
    print(i)

for i, item in enumerate(c):
    print(str(i)+" ---> "+str(item))

################## List ###########################

lst = "This is a list that is split".split()
print(lst)
print(lst[3])
print(lst[-1])
print(lst[-2])

print(lst[2:5])

lst2 = lst[:]
print(lst2 is lst)
print(lst2 == lst)


lst = [1, 5, 3, 7, 2]
lst.reverse()
print(lst)

lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)


def my_len(x):
    return len(str(x))


lst = [1, 25, 31, 17, 2, -11, -24]

lst.sort(key=my_len)
print(lst)
#################
