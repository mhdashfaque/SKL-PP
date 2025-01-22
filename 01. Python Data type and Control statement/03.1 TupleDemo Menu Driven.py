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

print("***************************")
print("Tuple Operations")
print("Shaikh Mohd Ashfaque")
print("***************************")

my_tuple = ("me", "my friend", "my brother", "my sister")
another_tuple = ("apple", "banana", "cherry")

while True:
    print("\nMenu:")
    print("1. Create tuple")
    print("2. Display tuple")
    print("3. Find length of tuple")
    print("4. Check if element is present in tuple")
    print("5. Concatenate tuples")
    print("6. Delete tuple")
    print("7. Count occurrences of an element in tuple")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ")

    if choice == '1':
        my_tuple = ("me", "my friend", "my brother", "my sister")
        print("\nTuple created.")
    elif choice == '2':
        print("\nDisplaying the tuple:")
        print(my_tuple)
        print("\nIndividual elements:")
        for item in my_tuple:
            print(item)
    elif choice == '3':
        length_of_tuple = len(my_tuple)
        print(f"\nLength of the tuple: {length_of_tuple}")
    elif choice == '4':
        element = input("\nEnter the element to check: ")
        if element in my_tuple:
            print(f"'{element}' is present in the tuple.")
        else:
            print(f"'{element}' is not present in the tuple.")
    elif choice == '5':
        concatenated_tuple = my_tuple + another_tuple
        print("\nConcatenated tuple:")
        print(concatenated_tuple)
    elif choice == '6':
        del my_tuple
        print("\nTuple has been deleted.")
        break
    elif choice == '7':
        element = input("\nEnter the element to count: ")
        count = my_tuple.count(element)
        print(f"\n'{element}' appears {count} times in the tuple.")
    elif choice == '8':
        print("\nExiting the program.")
        break
    else:
        print("\nInvalid choice. Please enter a number between 1 and 8.")
