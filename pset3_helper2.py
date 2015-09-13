def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    returnWord = []
    for letter in secretWord:
    	if letter in lettersGuessed:
    		returnWord.append(letter)
    	else:
    		returnWord.append(' _ ')
    return ''.join(returnWord)

    
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getGuessedWord(secretWord, lettersGuessed)
