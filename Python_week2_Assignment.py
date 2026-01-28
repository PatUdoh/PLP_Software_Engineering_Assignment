# Create an empty list
my_list = []

# Append element into the empty list 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("My List after append:", my_list)   # Output [10, 220, 30, 40]

# Insert the value 15 at the second position in the list.
my_list.insert(1, 15)
print("My List after insert:", my_list) #Ouput [10, 15, 20, 30, 40]

# Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])
print("My List after extend:", my_list)

#Remove the last element from my_list.
remove = my_list.pop(7)
print(f"Removed Last Element: {remove} Remaining: {my_list}")

# Sort my_list in ascending order.
new_list = sorted(my_list)
print( "New List:", new_list)

#Find and print the index of the value 30 in my_list.

if 30 in my_list:
    index = my_list.index(30)
    print("Index of 30:", index)
else:
    print("30 is not in the list")

