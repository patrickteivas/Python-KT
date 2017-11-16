file = open("kttekst.txt", "r")
text = file.read()
words = text.split()
print("Sõnade arv failis: " + format(len(words)))
wordsSfive = []
for word in words:
    if(len(word) < 5):
        wordsSfive.append(word)
print ("Väiksemate kui 5 tähte sõnade arv failis: " + format(len(wordsSfive)))
