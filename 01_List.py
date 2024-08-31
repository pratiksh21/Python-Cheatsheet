#List
--------------------------------------->>>>>>>>Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

------------------------------------------->>>>>>>Lists are created using square brackets:

 example : mylist = ["apple", "banana", "cherry"]
            print(mylist)

-------------------------------------------->>>>>>>>>>>  List items are ordered, changeable, and allow duplicate values.

-------------------------------------------->>>>>>>>   List items are indexed, the first item has index [0], the second item has index [1] etc.
---------------->>>> thislist = ["apple", 12, True]
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(len(thislist)) 
output - 3 


-------------------------Access Items
List items are indexed and you can access them by referring to the index number:

ExampleGet your own Python Server
Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])


-------------------------Negative Indexing
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.

Example
Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


Output - cherry


-----------------------------Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.

Example
Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

output -['cherry', 'orange', 'kiwi']


----------------------------Check if Item Exists
To determine if a specified item is present in a list use the in keyword:
if 34 in my_list:
    print("yes it is ")

-----------------------------Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:

Example
Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


-----------------------------Append Items
To add an item to the end of the list, use the append() method:

ExampleGet your own Python Server
Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


------------------------------------  extend list

list = [12,234,12,14,24,535]
my_list.extend(list)
print(my_list)



--------------------------------Add Any Iterable           ----------------------------------------------------------------------
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

Example
Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)



----------------------------Remove Specified Item
The remove() method removes the specified item.

ExampleGet your own Python Server
Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


---------------------------Remove Specified Index
The pop() method removes the specified index.

Example
Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

------------------------------  Looping
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


---------------------------------Loop Through the Index Numbers
You can also loop through the list items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.

for i in range(len(my_list)):
     print(my_list[i])


i =0

while i < len(my_list):
    print(my_list[i])
    i+=1






