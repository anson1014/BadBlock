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
    return mySet
  
def phrase_fix(dictionary):
  badSet = bad_words_store()
  phrase = input("Insert here: ")
  words = phrase.split()
  for x in range(len(words)):
      badword = words[x]
      if (badword in badSet):
        words[x] = wordReplace(badword)
        new_phrase = " ".join(words)
  print(new_phrase)

def wordReplace(word):
  switcher = {
    fuck: return "diddle"
    fucker: return "diddler"
    fucking: return "diddling"
    motherfucker: return "mother flubber"
    bitch: return "snitch"
    nigger or nigga: return "neighbour"
    dickpenis: return "male genitalia"
    pussy or vagina or cunt: return "female genitalia"
    else: return "BLEEP"
  }
