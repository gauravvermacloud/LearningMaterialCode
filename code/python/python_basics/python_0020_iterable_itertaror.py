iterable_list = "Summer Rainy Autom Winter".split()

iterator = iter(iterable_list)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
except StopIteration as si:
    print("StopIteration")

####################### Generator #################


def first_10_sqr_numbers():
    for x in range(10):
        yield x*x


for item in first_10_sqr_numbers():
    print(item)


############### Generator Comprehension ###################
gen = (x*x for x in range(10) if x % 2 == 0)
for i in gen:
    print(i)
