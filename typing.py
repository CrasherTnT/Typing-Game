import random
import time

def menu():
	menuDict = {"P": play,"R":rules, "D": display, "Q":quit} #Dictionary of function with their string equivalent...
	print("Welcome to Typing Master")
	print("""
    Menu for the game\n
    P)lay\n
    R)ules of the game\n
    D)isplay high scores\n
    Q)uit\n
    """)
	choice = input("Please choose one: > ") #This is the input
	
	"""
    This is where i got fucking stucked.. 
    First we call menuDict then get the input which
    is our choice variable then I used upper() method 
    to make lowercase character into uppercase
    Then lastly I put () to execute the function
	"""
	return menuDict[choice.upper()]() 
	
def rules():
    #Rules of the game
    print ("""
    Welcome \n
    Test your typing skills... \n
    Type as many words as you can in under 60 seconds and get your RAW words per minute and actual words per minute \n
    """)
    input("Press Enter to continue...\n")
    return menu()

def play():
    """Play function of the game."""
    usedTime = 0.0
    remainingTime = 0.0
    totalWords = 0
    incorrectWords = 0
    correctWords = 0
    wordLists = makelist()

    while (usedTime <= 10):
        word = randomword(wordLists)
        wordLists.remove(word)
        remainingTime = 10.0 - usedTime
        print (remainingTime)
        print (word)
        start = time.perf_counter()
        inputType = input("Enter a word:")
        end = time.perf_counter()
        if (inputType == word):
            correctWords += 1
        else:
        	incorrectWords += 1

        usedTime += (end - start)
        totalWords += 1

    raw=int((totalWords/usedTime) * 10.0)
    actual=int((correctWords/usedTime) * 10.0)
    print (f"""
    	TIMES UP!\n
    	Total no. of words: {totalWords} \n
    	No. of incorrect words: {incorrectWords} \n
    	RAW words per minute: {raw} \n
    	Actual words per minute: {actual} \n""")
    scores=readscore()
    addscore(scores,actual)
    writescore(scores)
    display()
    return menu()

def display():
	hiscore=readscore()    
	slist=sorted(hiscore)
	printscore(slist)
	return menu()

def makelist():
    """makes the list of words from words.txt file"""
    liopen = open("words.txt")
    theList = []
    for entry in liopen:
        entry = entry.strip()
        theList.append(entry)
    liopen.close()
    return theList

def randomword(theList):
    """chooses a random word from the wordlist"""
    return random.choice(theList)


def bubbleSort(theList):
    """Bubblesorts the list"""
    lastIndex = len(theList)-2
    while lastIndex >= 0:
        i = 0
        while i <= lastIndex:
            if theList[i][1] < theList[i+1][1]:
                theList[i], theList[i + 1] = theList[i + 1], theList[i]
            i +=1
        lastIndex -= 1

def readscore(fname = "highscore.txt"):
    hiscore = []
    fin = open(fname)

    for record in fin:
        record = record.strip() #strips non-printing characters
        data = record.split(",")

        entry = (data[0], int(data[1]))
        # the variable entry is a tuple. We can tell because it is being
        # assigned something within paranthesis
        # data a position at 0 is the "name" - no cats required
        # data at position 1 is the "score" - it needs to be casted as an int
        hiscore.append(entry)
    fin.close()
    return hiscore

def printscore(theList):
    """print the score on the screen"""
    count = 1
    print (f"""
    	Rank\tName\t\tScore
    	----\t----\t\t-----""")
    for entry in theList:
       print (f"""
       	{count}\t{entry[0]}\t{entry[1]}
       	""")
       count += 1

def newscore(theList, score):
    """Returns True if the score is to be added to the list, otherwise False"""
    bubbleSort(theList)
    if len(theList) < 10:
        return True
    else:
        if score > theList[-1][1]: #the value of the last score in the list.
            return True
    return False # score is not eligible

def addscore(theList, score):
    if newscore(theList, score):
        print("Congrats! You made the top 10.")
        name = input("What is your name:")
        entry=(name, score)
        theList.append(entry)
        bubbleSort(theList)

        if len(theList)>10:
            #only keep top 10 values
            theList.pop()

def writescore(theList):
    fout = open("highscore.txt", "w")

    for entry in theList:
        csvData = entry[0]+","+str(entry[1])+"\n"
        print (csvData)
        fout.write(csvData)
    fout.close()

if __name__ == "__main__":
	menu()
