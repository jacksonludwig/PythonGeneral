friends = ["Jack", "Mike", "Will", 15, False]
# friends[2] = "ABC"

# print(friends)
# print(friends[4])
# (friends[1:3])
# print(friends[-1])

newList = [1, 2, 3, 4, 5]
friends.extend(newList)
friends.append("New Name")
friends.insert(2, "other new name")
friends.remove("Mike")
print(friends)

friends.pop()
print(friends)

print(friends.index("Jack"))

print(friends.count("Mike"))
print(friends.count("Will"))

# friends.sort()
# print(friends)

friends.reverse()
print(friends)

listCopy = friends.copy()

friends.clear()
print(friends)

print(listCopy)
