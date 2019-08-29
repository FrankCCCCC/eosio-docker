file = open("keys", "r")
content = str(file.read())
strArr = content.split()
key = strArr[2]
print(key)