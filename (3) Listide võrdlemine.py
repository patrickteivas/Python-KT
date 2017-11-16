firstList = [11, 15, 6, 13, 13, 25, 32, 11, 20, 5, 31, 16, 32, 29, 11, 13, 3, 29, 28, 24]
secondList = [5, 19, 16, 4, 12, 7, 2, 28, 34, 29, 29, 36, 6, 8, 24, 18, 31, 7, 1, 7]

print("Sarnased numbrid:")
sameNum = []

for firstNum in firstList:
    for secondNum in secondList:
        if firstNum == secondNum:
            sameNum.append(firstNum)
cleanList = []
for x in sameNum:
    if x not in cleanList:
        cleanList.append(x)
print(cleanList)

numsList = firstList + secondList
print("Suurim number on: " + format(max(numsList)))
print("Väikseim number on: " + format(min(numsList)))
print ("Esimese listi keskmine: " + format(sum(firstList)/len(firstList)))
print ("Teise listi keskmine: " + format(sum(secondList)/len(secondList)))
print ("Mõlema listi keskmine: " + format(sum(numsList)/len(numsList)))
