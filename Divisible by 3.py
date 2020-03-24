# Initialization of  list
l = [10, 20, 30, 40, 50]

# Adding numbers inside list using indexing
if (l[0] + l[1] + l[2]) == 100:
    print("the numbers are ", l[0], l[1], l[2])
elif (l[1] + l[2] + l[3]) == 100:
    print("the numbers are", l[1], l[2], l[3])
elif (l[2] + l[3] + l[4]) == 100:
    print("the numbers are", l[2], l[3], l[4])
elif (l[3] + l[4] + l[0]) == 100:
    print("the numbers are", l[3], l[4], l[0])
elif (l[4] + l[1] + l[2]) == 100:
    print("the numbers are", l[4], l[1], l[2])
elif (l[4] + l[1] + l[3]) == 100:
    print("the numbers are", l[4], l[1], l[3])
elif (l[0] + l[2] + l[3]) == 100:
    print("the numbers are", l[0], l[2], l[3])
elif (l[0] + l[2] + l[4]) == 100:
    print("the numbers are", l[0], l[2], l[4])
elif (l[2] + l[4] + l[1]) == 100:
    print("the numbers are", l[2], l[4], l[1])
elif (l[2] + l[4] + l[2]) == 100:
    print("the numbers are", l[2], l[4], l[2])
elif (l[2] + l[4] + l[0]) == 100:
    print("the numbers are", l[2], l[4], l[2])
else:
    print("All numbers you entered there sum is not equal to 100")
