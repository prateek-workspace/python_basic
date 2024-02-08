# some list functions.

x = [10,20,30,40,50]
print(x)
print(len(x))

x.append(60)
print(x)
print(len(x))

# in insert() we have 2 values first is index second is our value.
x.insert(2,5)
# here 5 goes to index 2.
print(x)

# remove
# () removes particular value from list.
x.remove(5)
print(x)

# pop() removes the last value of the list.
x.pop()
print(x)


# reverse() reverses the entire list.
x.reverse()
print(x)