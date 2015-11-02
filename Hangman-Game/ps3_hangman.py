# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    i=0
    while i<len(secretWord):
        n=0
        G=False
        while n<len(lettersGuessed) and not G:
            if secretWord[i]==lettersGuessed[n]:
                G=True
            else: n+=1
            #print 'i=',i,'n=',n,'G=',G
        if G==True: i+=1
        else: return False
    return G


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result=''
    i=0
    while i<len(secretWord):
        n=0
        G=False
        while n<len(lettersGuessed) and not G:
            if secretWord[i]==lettersGuessed[n]:
                G=True
            else: n+=1
        if G==True: 
            result+=secretWord[i]# put secretWord[i] on position i
        else: 
            result+='_ '# put '_ ' on position i
        i+=1
    return result



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    allLetters=string.ascii_lowercase
    #print allLetters
    aL=''
    #print aL
    n=0
    while n<26 :
        i=0
        G=False
        #print len(lettersGuessed), G
        while i<len(lettersGuessed)and not G:
            if allLetters[n]==lettersGuessed[i]:
                G=True
            else: i+=1
            #print 'i=',i,'G=',G
        if G==False:
            aL+=allLetters[n]
            #print allLetters[n]
        n+=1
    return aL

def onetimeGuess(secretWord,LG):
    i=0
    G1=False
    while i<len(secretWord) and not G1:
    	if LG[0]==secretWord[i]: G1=True
    	else: i+=1
    return G1

def alreadyguess(lettersGuessed,LG):
    i=0
    PD=False
    while i<len(lettersGuessed) and not PD:
        if LG[0]==lettersGuessed[i]:
            PD=True
        else: i+=1
    return PD

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    	#secretWord=chooseWord(wordlist)
    LSW=len(secretWord)
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is',LSW,'letters long.'
    
    guesstime=8
    succeed=False
    lettersGuessed=[]
    
    while  guesstime>0 and not succeed:
        print '-------------'
        print 'You have',guesstime,'guesses left.'
        aL=getAvailableLetters(lettersGuessed)#get the available letters
        print 'Available letters:',aL# and show them

        LGG=raw_input('Please guess a letter:')#Enter a guess
        LG=[LGG.lower()]
        
        #print lettersGuessed
        #print secretWord
        G1=onetimeGuess(secretWord,LG)# show you the result of this time guess
        #print G1

        PD=alreadyguess(lettersGuessed,LG)#LG is already guessed or not
        lettersGuessed+=LG# put your guess in the already-guessed-list(lettersGuessed)
        result=getGuessedWord(secretWord,lettersGuessed)# show you the current result of the game 
        #print 'lettersGuessed',lettersGuessed,'LG=',LG,PD
        if PD==True:
            print "Oops! You've already guessed that letter:",result
        else:
            if G1==True:
    	        print 'Good guess:',result
            else:
    	        print 'Oops!That letter is not in my word:',result
    	        guesstime-=1#guess time-1
            succeed=isWordGuessed(secretWord,lettersGuessed)#test whether succeed
            if succeed==True:
                print '-----------'
                print 'Congratulations, you won!'
    if guesstime==0:
        print '-----------'
        print 'Sorry, you ran out of guesses. The word was',secretWord,'.'







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
