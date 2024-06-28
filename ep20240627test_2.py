# file = open("file.txt")
# content = file.read()   
# file.close()


with open("file.txt") as file:
    content = file.read()

print(content)