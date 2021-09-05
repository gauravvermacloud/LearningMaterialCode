import sys

def sum(x,y):
    return x+y

def __print_sum__(x,y):
    print(sum(x,y))

if(__name__ == "__main__"):
    #we are from command line
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    __print_sum__(x,y)