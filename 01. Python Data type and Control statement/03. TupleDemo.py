''' WAP to perform following operations on tuple
    (i)Create tuple
    (ii) Dispplay tuple
    (iii) Find Length of Tuple in Python
    (iv) Check Element Present in Tuple or Not
    (v) Concatenating Tuples in Python
    (vi)Deleting a Tuple
    (vii)use count method
'''

# Branch:
# Year:
# Sem:
# Subject :
# Name:
# UIN:
# Roll No.:

print("***************************");
print("Tuple");
print("Shaikh Mohd Ashfaque");
print("***************************");

# Python Tuple
print("\n i. Create tuple\n");
my_tuple = ("me", "my friend", "my brother", "my sister");
print("\nPrinting the tuple...");
print(my_tuple);
print("\nNow printing each item in the tuple...");
for item_in_tuple in my_tuple:
    print(item_in_tuple);

#tuple Display
print("\n (ii) Dispplay tuple\n");
tuple1 = ("python", "tuple", 1952, 2323, 432);
print(tuple1)              # this will print the complete tuple
print(tuple1[1:4])         # this will print the elements starting from 2nd till 4th
print(tuple1[1:])          # this will print the elements starting from the 2nd element
print(tuple1[0])           # this wil print the first element of the tuple
print(tuple1 * 2)          # this will print the tuple two times


# Finding length of a tuple example in python
print("\n iii. Find Length of Tuple in Python\n");
my_tuple = ("zero", "one", "two", "three", "four");
length_of_tuple = len(my_tuple);
print("Length of the tuple, my_tuple is:",length_of_tuple);

# check if an element is present inside a tuple or not
print("\n iv. Check Element Present in Tuple or Not\n");
my_tuple = ("zero", "one", "two", "three", "four");
if "one" in my_tuple:
    print("'one' is present as an element inside the tuple, my_tuple.");
else:
    print("Sorry! 'one' is not found in tuple, my_tuple.");

# Simple concatenation of tuple example in python
print("\n v. Concatenating Tuples in Python\n");
my_tuple = ("zero", "one", "two", "three", "four");
my_new_tuple = ("five", "six", "seven");
my_tuple += my_new_tuple;
print("Tuple after concatenating both the tuple:");
for mt in my_tuple:
    print(mt);


#delete a tuple
print("\n vi. Deleting a Tuple\n");
my_tuple = ('p','r','o','g','r','a','m','i','z')

# can't delete items
# if you uncomment line 8,
# you will get an error:
# TypeError: 'tuple' object doesn't support item deletion

#del my_tuple[3]

# can delete entire tuple
# NameError: name 'my_tuple' is not defined
del my_tuple

# count char
print("\n vii. use count method\n")
my_tuple = ('a','p','p','l','e',)

# Count
# Output: 2
print(my_tuple.count('a'))

# Index
# Output: 3
print(my_tuple.index('e'))
