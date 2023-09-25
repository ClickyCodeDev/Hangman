import random
a = ""
with open("words.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))

    a = random.choice(words)
word = []
for i in a:
    word.append(i)

guesses = 0
currentword = []
for i in word:
    currentword.append("_")
while True:
    i = 0
    print(currentword)
    ask = input("Guess a letter: \n")
    if ask.lower() in word:
        for e in word:
            if ask.lower() == e:
                currentword[i] = ask.lower()
            i += 1
    else:
        print("Wrong!")
        guesses += 1
    if guesses == 10:
        print(word)
        break
    if currentword == word:
        print(" \nYOU WIN!")
        break
