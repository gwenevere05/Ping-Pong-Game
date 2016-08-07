import random
import string
class Hangman(object):
  def __init__(self,num_of_turns_left): #hangman_pics=''
    # self.hangman_pics = hangman_pics

    
    # word_dict = {
    #       'food':'apple','banana'.'icecream','frenchfries'
    #       'drinks':'coffee','milkshake','cider','beer'

    # }
    self.words = words
    words ='apples','bananas','champagne','coffee','computer','python','hacker','telephone','tiger','portland','developer'.split()

    
    difficulty_step = 1
    num_of_turns_left = (6/difficulty_step)


  def start_game(self):
    choice = raw_input("Are you ready to play? Y/N?")
    if choice.upper() == "Y":
  		version_choice = int(raw_input("Pick 1 for the easy version(6 wrong guesses) or 2 for the hard version(3 wrong guesses): "))
  		if version_choice == 1:
  			difficulty_step = 1
  		if version_choice == 2:
  			difficulty_step = 2
    elif choice.upper() == "N":
      print "Good bye!"
      exit() 
    else:
  		print "Please input Y or N."
    self.choice = choice

  # def random_word(self,word_dict):
  #   category_choice = int(raw_input("Would you like to pick your category or have the computer pick? Choose 1 to pick your own or 2 for the computers choice:"))
  #   if category_choice == 1:
  #     self.word_dict = word_dict
  #     print word_dict.keys()
  #     player_category_choice = raw_input("Please enter a category")
  #     if player_category_choice.lower() in self.word_dict.keys():
  #       game_word = random.choice(self.word_dict[player_category_choice])
  #       self.secret_word = game_word
  #   elif category_choice == 2:
  #       rand_game_key = random.choice(self.word_dict.keys())
  #       game_word = random.choice(self.word_dict[rand_game_key])
  #       self.secret_word = game_word
  #       print "The category of your word is: %s" % (rand_game_key)
  #   else:
  #     print "Please input a valid answer."
    

  def random_word(self,words):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

  def update_board(self,num_of_turns_left):
    global hangman_pics
    self.board = hangman_pics[num_of_turns_left]
    return self.board
  	
  def blank_space_creator(self,secret_word):
    secret_word = self.secret_word
    num_of_blanks = "_" * len(secret_word)
    print num_of_blanks

  def player_guess(self,letter,secret_word,num_of_turns_left):
    self.letter = raw_input("Please enter a letter:").lower()
    self.secret_word = secret_word
    secret_word = list(secret_word)
    num_of_turns_left = num_of_turns_left
    self.already_guessed = []
    self.wrong_letters = []
  	
    for letter in secret_word:
      if letter in secret_word and letter not in already_guessed:
        str.replace("_","%s") % (letter)
        already_guessed.append(letter)
      elif letter not in secret_word and letter not in wrong_letters:
        wrong_letters.append(letter)
        already_guessed.append(letter)
        num_of_turns_left -= 1
        print "You are wrong! %s is not part of the word." % (letter)
      elif letter in already_guessed:
        letter2 = raw_input("You've already guessed that letter. Try again: ")
        print letter2
        #player_guess()
        #^^^?need to add something to get another guess/loop again

  def game_over(self,num_of_turns_left,secret_word):
    self.num_of_turns_left = num_of_turns_left
    if num_of_turns_left == 0:
      print "You lost. The secret word was %s." % (secret_word)

  def play_again(self,choice):
    self.choice = choice
    choice = raw_input("Would you like to play again? Y/N?")
    if choice.upper == "Y":
      self.__init__()
    elif choice.upper == "N":
      print "Goodbye!"
      exit()
    else:
      print "Please type in Y or N."




def main():
  hangman_pics = ['''

      +---+
      |   |
          |
          |
          |
          |
    =========''', '''

      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''

      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''

      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''

      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''

      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''

      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

  global num_of_turns_left
  Hangman(num_of_turns_left)
  hangman_game = Hangman(num_of_turns_left)
  print "Welcome to Hangman!"
  hangman_game.start_game()
  global words
  hangman_game.random_word(hangman_game.words)
  global num_of_turns_left
  while hangman_game.num_of_turns_left > 0:
    print hangman_game.update_board(hangman_game.num_of_turns_left)
    secret_word = hangman_game.random_word()
    hangman_game.blank_space_creator(secret_word)
  

if __name__ == '__main__':
  main()


      











