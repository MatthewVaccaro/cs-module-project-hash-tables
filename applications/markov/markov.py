import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# analyze which words can follow other words


def buildCache(string, cache={}):
    wordList = string.split()
    for i, word in enumerate(wordList):
        if i + 1 != len(wordList):
            if word not in cache:
                cache[word] = []
                cache[word].append(wordList[i + 1])
            else:
                if wordList[i + 1] not in cache[word]:
                    cache[word].append(wordList[i + 1])
    return cache


# construct 5 random sentences
def randomeSentence(d):
    wordList = words.split()
    fullSentence = []
    endingList = ['!', '.', '?']
    firstWord = random.choice(wordList)  # String
    fullSentence.append(firstWord)
    newWord = d[firstWord]  # Array

    while fullSentence[-1][-1] not in endingList:
        for word in newWord:
            fullSentence.append(word)
        nextWord = random.choice(wordList)
        newWord = d[nextWord]

    return " ".join(fullSentence)


print(randomeSentence(buildCache(words)))
