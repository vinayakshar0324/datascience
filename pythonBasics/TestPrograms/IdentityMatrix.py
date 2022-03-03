# WAP For Identity Matrix

matSize = int(input("Enter the Matrix size:"))

for i in range(0, matSize):
    for j in range(0, matSize):
        if (i==j):
            print("1", sep=' ', end=' ')
        else:
            print("0", sep=' ', end=' ')
    
    print()