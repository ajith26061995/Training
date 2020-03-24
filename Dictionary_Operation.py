# importing "operator" for implementing itemgetter
import operator

# Initializing list of dictionaries
d = [{'name': 'Vasanth', 'age': '56'}, {'name': 'Ajith', 'age': '35'}]

# using sorted and itemgetter to print list sorted by age
print(sorted(d, key=operator.itemgetter('age')))

# using sorted and itemgetter to print list sorted by name
print(sorted(d, key=operator.itemgetter('name')))