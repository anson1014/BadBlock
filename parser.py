def bad_words_store():
    f = open("badwordstwo.csv", "r")
    mySet = set()
    for x in f:
        mySet.add(x)
    
    print(len(mySet))