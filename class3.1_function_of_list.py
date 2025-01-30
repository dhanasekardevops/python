#len(list): Returns the number of elements.

mylist=[23,48,39,24]
mylist1=(23,48,39,24)
mylist_length=len(mylist)
print(mylist_length)

#max(list): Returns the largest element
mylist_max=max(mylist)
print(mylist_max)

#min(list): Returns the smallest element.
mylist_min=min(mylist)
print(mylist_min)

#sum(list): Returns the sum of elements (only for numeric lists).
mylist_sum=sum(mylist)
print(mylist_sum)

#sorted(list): Returns a sorted list (does not modify the original).
mylist_sort=sorted(mylist)
print(mylist_sort)

#list(iterable): Converts an iterable (like a tuple, set) into a list.
mylist_tuple=list(mylist1)
print(type(mylist_tuple),mylist_tuple)
