#Methods
#set.add(item): Adds an item to the end.
dhanaset={2345,6789,1234,5678}
dhanaset.add(9876)
print(dhanaset)

# # set.update(index, item): updates an item at a specific index.
# dhanaset.update(2,9876)
# print(dhanaset)

# set.update(iterable): Adds all elements of an iterable to the set.
dhanaset1={2,3,4}
dhanaset.update(dhanaset1)
print(dhanaset)

# set.remove(item): Removes the first occurrence of an item.
dhanaset.remove(5678)
print(dhanaset)
# set.pop(index=-1): Removes and returns the item at the index (default: first item).
dhanaset.pop()
print(dhanaset)
# set.clear(): Removes all items.
dhanaset.clear()
print(dhanaset)
# set.index(item, start=0, end=len(set)): Returns the index of the first occurrence of an item.
dhanaset2=[2345,6789,1234,5678,5678,5678,5678,2345]
print(dhanaset2.index(5678))
# print(dhanaset2.count(2345))

# set.count(item): Returns the count of an item.

print(dhanaset2.count(5678))
print(dhanaset2.count(2345))



#set.discard(item): Removes an item; does nothing if not found.

Output:
{6789, 2345, 5678, 1234, 9876}
{2, 3, 4, 6789, 2345, 5678, 1234, 9876}
{2, 3, 4, 6789, 2345, 1234, 9876}
{3, 4, 6789, 2345, 1234, 9876}
set()
3
4
2

