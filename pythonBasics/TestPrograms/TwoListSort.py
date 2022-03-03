# WAP To merge two list ans sort it

myList1 = []
myList2 = []

listSize = int(input("Enter list Size of ListSize1:"))
for i in range(1, listSize+1):
    element1 = int(input("Enter Elements for list 1:"))
    myList1.append(element1)

listSize = int (input("enter The list Size of ListSize2:"))
for i in range(1, listSize+1):
    element2 = int(input("Enter Element For List 2:"))
    myList2.append(element2)
    
mergeList = myList1 + myList2

mergeList.sort()

print("Your new Sorted List Is:", mergeList)