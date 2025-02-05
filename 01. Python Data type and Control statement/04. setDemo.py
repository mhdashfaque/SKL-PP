''' WAP on set to perform following operations
    (i) create set
    (ii)union, intersection, difference, symmetric difference
    (iii) change set
    (iv) remove elements from a set
    (v) Use pop and clear
    (vi) test if an item exists in a set or not   
'''
# Branch:
# Year:
# Sem:
# Subject :
# Name:
# UIN:
# Roll No.:

print("***************************")
print("set Operations")
print("Shaikh Mohd Ashfaque")
print("***************************")

'''
    (i) create set
    (ii)union, intersection, difference, symmetric difference
'''
while True:
    A = {0, 2, 4, 6, 8}
    B = {1, 2, 3, 4, 5}
    print("If A = {0, 2, 4, 6, 8}")
    print("and B = {1, 2, 3, 4, 5}")
    print("Then,")
    print("Union of A and B =", A | B)
    print("Intersection of A and B =", A & B)
    print("Difference of A and B =", A - B)
    print("Symmetric difference of A and B =", A ^ B)
    print("\n want to watch again:y/n")
    check=input()
    if check=='n':
        break;

''' (iii) change set '''
# initialize my_set
my_set = {1,3}
print(my_set)

# if you uncomment line 9,
# you will get an error
# TypeError: 'set' object does not support indexing

#my_set[0]

# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2,3,4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4,5], {1,6,8})
print(my_set)


# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

'''remove elements from a set '''
# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# If you uncomment line 27,
# you will get an error.
# Output: KeyError: 2

#my_set.remove(2)

'''Use pop and clear'''
# initialize my_set
# Output: set of unique elements
my_set = set("HelloWorld")
print(my_set)

# pop an element
# Output: random element
print(my_set.pop())

# pop another element
# Output: random element
my_set.pop()
print(my_set)

# clear my_set
#Output: set()
my_set.clear()
print(my_set)

''' test if an item exists in a set or not'''
# initialize my_set
my_set = set("apple")

# check if 'a' is present
# Output: True
print('a' in my_set)

# check if 'p' is present
# Output: False
print('p' not in my_set)
