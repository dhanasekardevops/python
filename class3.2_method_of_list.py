#Methods
#list.append(item): Adds an item to the end.
dhanalist=[2345,6789,1234,5678]
dhanalist.append(9876)
print(dhanalist)

# list.insert(index, item): Inserts an item at a specific index.
dhanalist.insert(2,9876)
print(dhanalist)

# list.extend(iterable): Adds all elements of an iterable to the list.
dhanalist1=[2,3,4]
dhanalist.extend(dhanalist1)
print(dhanalist)

# list.remove(item): Removes the first occurrence of an item.
dhanalist.remove(5678)
print(dhanalist)
# list.pop(index=-1): Removes and returns the item at the index (default: last item).
dhanalist.pop()
print(dhanalist)
# list.clear(): Removes all items.
dhanalist.clear()
print(dhanalist)
# list.index(item, start=0, end=len(list)): Returns the index of the first occurrence of an item.
dhanalist2=[2345,6789,1234,5678,5678,5678,5678,2345]
print(dhanalist2.index(5678))
# print(dhanalist2.count(2345))

# list.count(item): Returns the count of an item.

print(dhanalist2.count(5678))
print(dhanalist2.count(2345))



# list.sort(reverse=False): Sorts the list in ascending order.
# list.reverse(): Reverses the order of elements.
# list.copy(): Returns a shallow copy of the list.
