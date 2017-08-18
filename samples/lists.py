# empty lists are created like this
my_list = []
print(my_list)

# create and initialize a list like this
vehicles = ["car", "motorcycle"]
print(vehicles)

# len(my_list) will return the list size
size = len(vehicles)
print(size)

# get list items by index (starting with zero)
my_list = ['1', '2', '3', '4', '5', '6']
print(my_list[0])
print(my_list[4])

# my_list[-1] will return the last element
# my_list[-2] will return the item before last item and so on
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

# add a list item to the end using append()
my_list = ['a', 'b', 'c']
my_list.append('d')
print(my_list)

# insert an item at a specific index
my_list = ['a', 'b', 'c']
my_list.insert(1, 'd')
print(my_list)

# delete an item by it's value -- only first occurence will be deleted!
list_with_duplicates = ['a', 'b', 'c', 'a']
list_with_duplicates.remove('a')
print(list_with_duplicates)

# delete an item by it's index - starting with zero!
my_list = ['a', 'b', 'c']
del my_list[1]
print(my_list)

# list.pop() will remove and return the last item
my_list = ['a', 'b', 'c']
popped_item = my_list.pop()
print(my_list)
print(popped_item)

# pop(index) works also with indexes
my_list = ['a', 'b', 'c']
popped_item = my_list.pop(1)
print(my_list)
print(popped_item)

# sorting a list alphabetically
# caution: this sorting cannot be reverted!
my_list = ['c', 'b', 'a']
my_list.sort()
print(my_list)

# sorted(list) will return the sorted list but will not modifiy the
# original list
my_list = ['c', 'b', 'a']
sorted_list = sorted(my_list)
print(sorted_list)
print(my_list)

# to reverse the items of a list you can call list.reverse()
# to get the original order you can simply call .reverse again
my_list = ['a', 'b', 'c']
my_list.reverse()
print(my_list)

# you can loop through lists using the for-loop - don't forget the 
# colon at the end also you need to add spaces for the body of the loop
number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for num in number_list:
	print('this is the number: ' + num)
print("this has no spaces - so it's not within the loop")

# you can also define a range for a loop:
# the range is created including the first parameter until it reaches/
# exceeds the second parameter (= this one is not included!)
# if you use 2 parameters, the loop variable will be increased by 1
for i in range(0, 10):
	print(i)
print('loop end')

# you increase the loop variable by using the third parameter:
for i in range(0, 10, 2):
	print(i)
print('loop end')

# you can also create a list using range:
my_list = list(range(3,6))
print(my_list)

# for numeric numbers you can use some pre-build functions:
number_list = list(range(0,10))
print(number_list)
print(sum(number_list))
print(min(number_list))
print(max(number_list))

# list comprehension = creating lists using range function
number_list = [value+1 for value in range(0,10)]
print(number_list)

# slicing lists:
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(my_list)
# first 3 elements (first argument included, second excluded)
print(my_list[0:3])
# first 4 elements
print(my_list[:4])
# element #3 to list end
print(my_list[2:])
# also negative index is possible: this selects last 3 elements
print(my_list[-2:])

# you can also loop through a slice
for i in my_list[3:]:
	print(i)

# [:] will create a copy of the entire list
my_list = ['a', 'b', 'c']
copy_list = my_list[:]
my_list.append('this should only be in this list')
print(my_list)
print(copy_list)








