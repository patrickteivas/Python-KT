print("Sisestage kaks arvu")
x = int(input())
y = int(input())
if (x < y):
   numList = range(x + 1, y)
else:
    numList = range(y + 1, x)
for num in numList:
    if (num % 2 == 0):
        print(num)
