makeneutral = {"fuck":"sticks", "shit":"trash", "bitch":"dingledoo" }
makegood = {"fuck":"love","shit":"sunshine", "bitch":"happy" }
modes = ["MAKENEUTRAL", "MAKEGOOD"]
def mode():
  choice = input("[1]: MakeNeutral or [2]: MakeGood")
  
  print(choice)
  
  current = ""
  
  if choice == 1:
    current = modes[0]
    print(current)
  elif choice == 2:
    current = modes[2]
    print(current)
  
  print('Your current mode is: ' + current)

def profanity_fix(dictionary):
  print('What phrase would you like to fix?')
  phrase = input("Insert here: ")
  phrase = phrase.split() # list
  bad_words = []
  for split in phrase:
    if (split in dictionary):
      bad_words.append(split)
  good_words = []
  for bad_word in bad_words:
    good_words.append(dictionary.get(bad_word))
  
  new_phrase = ""
  for i in range(len(good_words)):
    print("index: " + str(i))
    print("phrase " + str(phrase))
    new_phrase = ' '.join(phrase)
    new_phrase = new_phrase.replace(bad_words[i],good_words[i]) 
    #phrase = new_phrase
    print("new phrase: " + str(new_phrase))
    print("bad words: " + str(bad_words))
    print("good words: " + str(good_words))

    

#   fuckprint("phrase: " + phrase)
  
def phrase_fix(dictionary):
  phrase = input("Insert phrase to BadBlock here: ")
  words = phrase.split()
  for x in range(len(words)):
      badword = words[x]
      if (badword in dictionary):
        words[x] = dictionary.get(badword)
        new_phrase = " ".join(words)
  print(new_phrase)

phrase_fix(makeneutral)

def bad_words_store():
    f = open("badwordstwo.csv", "r")
    mySet = set()
    for x in f:
        mySet.add(x)
    
    print(len(mySet))



  
def phrase_fix(dictionary):
  phrase = input("Insert here: ")
  words = phrase.split()
  for x in range(len(words)):
      badword = words[x]
      if (badword in dictionary):
        words[x] = dictionary.get(badword)
        new_phrase = " ".join(words)
  print(new_phrase)