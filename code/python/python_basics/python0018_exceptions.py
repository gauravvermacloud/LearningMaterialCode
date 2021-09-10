try:
    x = 0/0
    print(x)
except ZeroDivisionError as z:
    print(str(z))
finally:
    print("some work done")
