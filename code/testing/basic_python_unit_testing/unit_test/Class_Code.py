class my_fact:

    def fact(self, x):
        if(x < 0):
            raise ValueError("x is less than 0")
        else:
            return 1 if x == 0 else x * self.fact(x-1)


f = my_fact()
f.fact(5)
print(f.fact(5))
