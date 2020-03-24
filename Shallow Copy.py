# importing "copy" for copy operations
import copy

# initializing list 1
List1 = [1, 2, [3, 5], 4]

# using copy to shallow copy
List2 = copy.copy(List1)

# original elements of list
print("The original elements before shallow copying")
print(List1)

# adding an element to new list
List2[2][0] = 7

# checking if change is reflected
print("The original elements after shallow copying")
print(List1)