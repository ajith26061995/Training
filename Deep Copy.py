# importing "copy" for copy operations
import copy

# initializing list 1
List1 = [1, 2, [3, 5], 4]

# using deepcopy to deep copy
List2 = copy.deepcopy(List1)

# original elements of list
print("The original elements before deep copying")
print(List1)

# adding an element to new list
List2[2][0] = 7

# Change is reflected in l2  
print("The new list of elements after deep copying ")
print(List2)

# Change is NOT reflected in original list 
# as it is a deep copy 
print("The original elements after deep copying")
print(List1)

