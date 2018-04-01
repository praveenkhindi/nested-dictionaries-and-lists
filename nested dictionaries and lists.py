#Here’s a program that uses a dictionary that contains other dictionaries in order to see who is bringing what to a picnic.
#The totalBrought() function can read this data structure and calculate the total number of an item being brought by all the guests.


allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}

def total_brought(guests, items):
    num_brought = 0
    for k,v in guests.items():
        num_brought = num_brought + v.get(items,0)
        return num_brought

print('total number of things')
print('apples '+ str(total_brought(allGuests, 'apples')))
print('pretzels '+ str(total_brought(allGuests, 'pretzels')))
print('ham sandwiches '+ str(total_brought(allGuests, 'ham sandwiches')))
print('cups '+ str(total_brought(allGuests, 'cups')))
print('apple pies '+ str(total_brought(allGuests, 'apple pies')))
