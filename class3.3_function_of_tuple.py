#len(list): Returns the number of elements.

mylist_tuple=(23,48,39,24)
mylist_tuple1=(23,48,39,24)
mylist_tuple_length=len(mylist_tuple)
print(mylist_tuple_length)

#max(list): Returns the largest element
mylist_tuple_max=max(mylist_tuple)
print(mylist_tuple_max)

#min(list): Returns the smallest element.
mylist_tuple_min=min(mylist_tuple)
print(mylist_tuple_min)

#sum(list): Returns the sum of elements (only for numeric lists).
mylist_tuple_sum=sum(mylist_tuple)
print(mylist_tuple_sum)

#sorted(list): Returns a sorted list (does not modify the original).
mylist_tuple_sort=sorted(mylist_tuple)
print(mylist_tuple_sort)

#list(iterable): Converts an iterable (like a tuple, set) into a list.
mylist_tuple_tuple=list(mylist_tuple1)
print(type(mylist_tuple_tuple),mylist_tuple_tuple)

Output :
4
48
23
134
[23, 24, 39, 48]
<class 'list'> [23, 48, 39, 24]
