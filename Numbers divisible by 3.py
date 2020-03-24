# Take a list of numbers
my_list = [12, 3, 65, 54, 39, 102, 339, 221,]

# use anonymous function to filter
result = list(filter(lambda x: (x % 3 == 0), my_list))

# display the result
print("Numbers divisible by 3 are",result)