list_z = list("hello world")
d2 = {1:'a',2:'b',3:'c'}

for item in list_z:
    print(item)
    
for item in d2:
    print (str(item) +" --> "+ str(d2[item]))
    
    
#Custom iterator

class MyIterable:
    def __init__(self):
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.current = self.current+1
        if (self.current < 10):
            return self.current
        else:
            raise StopIteration

for x in MyIterable():
    print(x)