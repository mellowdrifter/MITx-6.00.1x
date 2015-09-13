def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in
    lettersGuessed; False otherwise
    '''
    if len(secretWord) == 0:
        return True
    else:
        return secretWord[0] in lettersGuessed \
            and isWordGuessed(secretWord[1:], lettersGuessed)


secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print isWordGuessed(secretWord, lettersGuessed)


secretWord = 'apple'
lettersGuessed = ['l', 'i', 'k', 'p', 'a', 'e']
print isWordGuessed(secretWord, lettersGuessed)
