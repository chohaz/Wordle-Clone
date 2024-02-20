'''
The program contains classes that facilitate the gameplay, 
including functions or methods for handling words, guesses, and the game mechanics.

Name: Hazel Cho
Date: Nov 13, 2023
'''


from collections.abc import MutableSet
from random import choice


class TooShortError(ValueError):
    pass
    
class TooLongError(ValueError):
    pass
    
class NotLettersError(ValueError): 
    pass 

class WordleWords(MutableSet):
    def __init__(self, letters):
        ''' 
        initializes an empty set of words. 
        letters specifies how long they should all be.
        '''
        self._words = set()
          #... more code here ...
        self.length = letters
        
    def __contains__(self, word):
        '''
        returns True if the word is in the set, returns False otherwise.
        '''
        return word in self._words
    def __iter__(self):
        '''
        returns an iterator over all the words in the set.
        '''
        return iter(self._words)
    def __len__(self):
        '''
        return the number of words in the set.
        '''
        return len(self._words)
    def add(self, word):
        ''' some code to check the word '''
        self._words.add(word)
        
    def discard(self, word):
        '''
        add the word to the set. 
        Raises an error if the word is too short, or too long, 
        or doesn’t contain only capital letters A-Z.
        '''
        self._words.discard(word)
        
    def load_file(self, filename):
        '''
        Add words to the set using the content of the file specified by the filename.
        '''
        with open(filename,'r') as f:
            for line in f:
                rs = line.rstrip()
                if len(rs) == self.length:
                    self._words.add(rs)
      
    def check_word(self, word):
        '''
        Takes a word and makes sure that it consists only of the capital letters A-Z (no accents) and is the correct length.
      '''
        if len(word) < self.length:
            raise TooShortError
        elif len(word) > self.length:
            raise TooLongError
        
        cap = word.isupper()
        alpha = word.isalpha()
        
        if alpha == False or cap == False:
            raise NotLettersError       

        
    def letters(self):
        '''
        Returns the number of letters in every word.
        (Which should be the same for every word!)
        '''
        size = len(self._words)
        i = 0
        for w in self._words:
            for letter in w:
                i = i + 1

        letters = i / size 
        return letters
    
    def copy(self):
        '''
        Returns a second WordleWords instance that contains the same words. It should not re-load the file!
        '''
        new = WordleWords(self.length)
        for word in self:
            new.add(word)
        
        return new
          
class Guess():
    def __init__(self, guess, answer):
        '''
        should take two parameters, the guess the player made and the correct answer.
        '''
        self._guess = guess
        self._answer = answer
    
    def guess(self):
        '''
        should return the guess that the player made.
        '''
        guess = self._guess
        return guess
      
    def correct(self):
        '''
        should return a string that is the same length as the answer. It should
        consist of underscores, except for where the player guessed correctly.
        '''
        under = '_'*len(self._answer)
        liunder = list(under)        
        
        ind = []
        
        for i in range(len(self._guess)):
            if self._guess[i] == self._answer[i]:
                ind.append(i)
        
        for i in ind:
            liunder[i] = self._answer[i]
        
        strunder = ''.join(liunder)
        return strunder
        
    def misplaced(self):
        '''
        should return a sorted string that contains every letter that the
        player guessed that is also in the answer, but not at the same position.
        '''
        
        mis = []
        ans = list(self._answer)
        guess = list(self._guess)
        temp = []
        for i in range(len(guess)): # takes the index of a correct answer
            if guess[i] == ans[i]:
                temp.append(i)

        for i in temp: # removes the correct answer from the variable
            ans.remove(self._answer[i]) 
            guess.remove(self._guess[i])
            
        for i in guess:
            for w in range(len(ans)):
                if i == ans[w]:
                    if guess[w] != ans[w]:
                        mis.append(i)
        
        sort = sorted(mis) # sort the list
        misstr = ''.join(sort) # join the list and make it in to a string
        return misstr
      
      
    def wrong(self):
        '''
        should return a sorted string that contains every letter that the player
        guessed that was not in the answer.
        '''
        wro = []
        ans = list(self._answer)
        guess = list(self._guess)
        temp = []
        for i in range(len(guess)): # takes the index of a correct answer
            if guess[i] == ans[i]:
                temp.append(i)
        
        for i in temp: # removes the correct answer from the variable
            ans.remove(self._answer[i]) 
            guess.remove(self._guess[i])
            
        for i in guess:
            if i not in ans:
                wro.append(i)
        
        sort = sorted(wro)
        wrostr = ''.join(sort)
        return wrostr
      
    def is_win(self):
        '''
        should return True if the guess was the same as the answer
        '''
        
        if self._guess == self._answer:
            return True
        else:
            return False
    
class Wordle():
    def __init__(self, words):
        wordsli = list(words)
        self.word = choice(wordsli)
        self.count = 0
    
    def guesses(self):
        '''
        return the number of guesses the player has made so far.
        '''
        return self.count
    
    def guess(self, guessed):
        '''
        take a string guessed and return a Guess instance
        object that represents the results of the guess.
        '''
        self.count = self.count + 1
        g = Guess(guessed,self.word)
        return g
