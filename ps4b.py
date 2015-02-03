from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    maxScore = 0
    bestWord = ''
    def canConstructFromHand(hand, word):
        newHand = hand.copy()
        for letter in word:
            value = newHand.get(letter,0)
            newValue = value - 1
            if newValue < 0:
                return False
            newHand[letter] = newValue
        return True

    for word in wordList:

        if canConstructFromHand(hand, word):
                if getWordScore(word,n) > maxScore:
                    maxScore = getWordScore(word,n)
                    bestWord = word
    if bestWord == '':
        return None
    return bestWord



#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    totalScore = 0
    
    while calculateHandlen(hand) != 0:
        print "Current Hand:",
        displayHand(hand)
        computerWord = compChooseWord(hand, wordList, n)
        if computerWord == None:
            break
        else:
           
            if not isValidWord(computerWord, hand, wordList):
                print("Invalid word, please try again.")
                print('')
            else:
                totalScore += getWordScore(computerWord, n)
                print("\"{}\" earned {} points. Total: {} points".format(computerWord, getWordScore(computerWord, n), totalScore))                
                print('')
                
                hand = updateHand(hand, computerWord)
    
    print("Total score: "+str(totalScore)+" points.")
        



    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
               










        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
        
    playGame(wordList)


