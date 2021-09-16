from sys import argv

value = argv[1:]
sum=0
for x in value:
    sum = sum + int(x)
print("Result:",sum)