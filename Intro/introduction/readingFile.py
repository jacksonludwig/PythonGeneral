file = open("exampleText.txt", "r")

print(file.readable())
# print(file.read())
# print(file.readlines()[3])

for name in file.readlines():
    print(name)

file.close()




