# WAP To Find the Second largest Number in the list

listsize = int(input("Enter The list size:"))

myList = []

for i in range(1, listsize+1):
    element = int(input("Enter The element:"))
    myList.append(element)
    
myList.sort()

print("Second Largest Element is:", myList[listsize-2])