# WAP To Calculate the average of numbers in a given list.

listSize = int(input("Enter The List Size First:"))

myList = []

for i in range(0,listSize):
    myNum = int(input("Enter The NumBer:"))
    myList.append(myNum)

average = sum(myList)/listSize

print("Average Of This List is:", round(average,3))
