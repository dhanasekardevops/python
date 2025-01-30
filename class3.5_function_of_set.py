#len(list): Returns the number of elements.

myset={23,48,39,24,23}
myset1=(23,48,39,24)
myset3={23,48,39,24,23}
myset_length=len(myset)
print(myset_length)

#max(list): Returns the largest element
myset_max=max(myset)
print(myset_max)

#min(list): Returns the smallest element.
myset_min=min(myset)
print(myset_min)

#sum(list): Returns the sum of elements (only for numeric lists).
myset_sum=sum(myset)
print(myset_sum)

#sorted(list): Returns a sorted list (does not modify the original).
myset_sort=sorted(myset)
print(myset_sort)

#list(iterable): Converts an iterable (like a tuple, set) into a list.
myset3=set(myset3)
print(type(myset3),sorted(myset3))
