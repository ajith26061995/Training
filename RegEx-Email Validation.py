import re

# Make a regular expression
# for validating an Email
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


# Define a function for
# for validating an Email
def check(email):
    # pass the regualar expression
    # and the string in search() method
    if (re.search(regex, email)):
        print("Valid Email Id")

    else:
        print("Invalid Email")

    # Driver Code


if __name__ == '__main__':
    # Enter the email
    email = input("Enter Your Email Id  : ")
    # calling run function
    check(email)
