''' WAP in python to implement following
    (i) create a list
    (ii) Display list
    (iii) Find length of list
    (iv)Check Element is in List or Not
    (v) Concatenating Lists in Python
    (v) Replacing List Element with new one in Python
    (vi)Deleting Element from List in Python
    (vii) Python Nested Lists
'''
# Branch:
# Year:
# Sem:
# Subject :
# Name:
# UIN:
# Roll No.:

print("***************************");
print("List Operations");
print("Shaikh Mohd Ashfaque");
print("***************************");

#Creating a List in Python
print("\ni. create a list\n");
list1 = ["python", "list", 1952, 2323, 432]
list2 = ["this", "is", "another", "list"]

# Displaying List
print("\nii. Display list\n");
print("list1:",list1)              # this will print the complete list
print("List2:",list2)              # this will print the complete list
print(list1[1:4])         # this will print the elements starting from 2nd till 4th
print(list1[1:])          # this will print the elements starting from the 2nd element
print(list1[0])           # this wil print the first element of the list
print(list1 * 2)          # this will print the list two times
print(list1 + list2)      # this will print the concatenated list

print("Elements of the list, List1 are:");
for ml in list1:
    print(ml);

# length of List
print("\niii. Find length of list\n");
length_of_list1 = len(list1);
print("Length of the list, my_list1 is:",length_of_list1);

#Check Element is in List or Not
print("\niv.Check Element is in List or Not");
if "another" in list2:
    print("'another' is in the list2.");
else:
    print("'another' is not in the list2.");

#Concatenating Lists in Python
print("v. Concatenating Lists in Python\n");
my_list = ["zero", "one", "two", "three", "four"];
my_new_list = ["five", "six"];
my_list += my_new_list;
print("List's items after concatenating:");
for l in my_list:
    print(l);

#Replacing List Element with new one in Python
print("\nvi. Replacing List Element with new one in Python\n");
my_list = ["zero", "one", "two", "three", "four"];
print("Elements of the list, my_list are:");
for ml in my_list:
    print(ml);
my_list[0] = "one";
my_list[4] = "five";
print("\nNow elements of the list, my_list are:");
for ml in my_list:
    print(ml);

#Deleting Element from List in Python
print("\nvii. Deleting Element from List in Python\n");
my_list = ["zero", "one", "two", "three", "four"];
print("Elements of the list, my_list are:");
for ml in my_list:
    print(ml);
index = input("\nEnter index no:");
index = int(index);
print("Deleting the element present at index number",index);
del my_list[index];
print("\nNow elements of the list, my_list are:");
for ml in my_list:
    print(ml);

#Python Nested Lists
print("\nviii. Python Nested Lists\n");
books_list = [("C", 896), ("C++", 599), ("Python", 1269)];
print("Books list with prices.");
ch = None;
while ch != "0":
    print("\n0 - Exit");
    print("1 - Show Books List");
    print("2 - Add a Book");
    ch = input("Choice:");
    if ch == "0":
        print("Exiting...");
    elif ch == "1":
        print("\nBook\t\tPrice");
        for add_book in books_list:
            book_name, book_price = add_book;
            print(book_name,"\t\t",book_price);
    elif ch == "2":
        book_name = input("\nEnter name of the book:");
        book_price = int(input("Enter its price:"));
        add_book = (book_name, book_price);
        books_list.append(add_book);
    else:
        print("Sorry, but",choice,"is not valid choice.");
