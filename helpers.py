from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # split strings by newlines into lists, then into two respective sets as to avoid dupes
    setA = set()
    for word in a.splitlines():
        setA.add(word)

    setB = set()
    for word in b.splitlines():
        setB.add(word)

    # create a list that will take in matching lines between set A and set B
    sameLines = []

    for line in setA:
        if line in setB:
            sameLines.append(line)

    # return the list of matching lines
    return sameLines


def sentences(a, b):
    """Return sentences in both a and b"""

    # splits string 'a' into sentences and adds them to a set A. Does same for string 'b' and set B
    setA = set()
    for sentence in sent_tokenize(a):
        setA.add(sentence)

    setB = set()
    for sentence in sent_tokenize(b):
        setB.add(sentence)

    # finds sentences in both sets and adds it to a list of same santences, then returns that list
    sameSentence = []
    for sentence in setA:
        if sentence in setB:
            sameSentence.append(sentence)

    return sameSentence


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # makes a list that will take in same substrings
    sameSubstring = []

    # for each substring in setA, if it is in setB as well, add it to the list above
    for substring in do_substring(a, n):
        if substring in do_substring(b, n):
            sameSubstring.append(substring)

    # return the list of same substrings
    return sameSubstring


def do_substring(a, n):
    # helper function for substrings, takes in a string and a number

    # create an empty set to take in unique substrings, and breaks down the length of the full string
    setA = set()
    lenA = len(a)
    count = 0

    # while we have not reached the end of the full string, add unique substrings to the set go up by 1 element
    while (count + n) <= lenA:
        setA.add(a[count: (count + n)])
        count += 1

    # return the set of substrings
    return setA
