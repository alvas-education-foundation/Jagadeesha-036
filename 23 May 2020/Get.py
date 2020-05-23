myfile = open ("original.txt")
content = myfile.read()
myfile.close()

with open("original.txt") as myfile:
    content = myfile.read()

print(content)
