count = 0

def print_count():
    print(count)

def set_count_no_global(c):
    count = c

def set_count_global(c):
    global count
    count =c

print_count()

set_count_no_global(5)

print_count()

set_count_global(5)

print_count()