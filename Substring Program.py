# initializing string
test_str = "Google is good website"

# initializing  substrings
test_list = ["Google", "site", "Gmail", "Youtube", "Facebook"]

# printing original string
print("The original string is : " + test_str)

# printing  strings list
print("The original list is : " + str(test_list))

# using list comprehension
# Get matching substrings in string
res = [sub for sub in test_list if sub in test_str]

# printing result
print("The list of found substrings : " + str(res))