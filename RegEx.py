import re

def isValid(Number):

    # 1) Begins with 0 or 91
    # 2) Then starts with 6 or 7 or 8 or 9
    # 3) Then contains 9 digits
    Pattern = re.compile("(0/91)?[6-9][0-9]{9}")
    return Pattern.match(Number)

# Driver Code
Number = input("enter:")
if (isValid(Number)):
    print ("Valid Number")
else :
    print ("Invalid Number")
