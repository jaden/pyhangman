#!/usr/bin/python

import config
import random
import string

def debug(msg):
  if config.DEBUG:
    print(msg)

def word_filter(word):
  word = word.rstrip()

  if "'" in word:
    debug("Filtering `%s` because it has an apostrophe" % word)
    return False

  if len(word) < config.MIN_WORD_LENGTH:
    debug("Filtering `%s` because it has less than %d letters" % (word, config.MIN_WORD_LENGTH))
    return False

  return True

def pick_word():
  words_file = open(config.WORDS_FILE, "r")
  words = words_file.readlines()
  words = [word for word in words if word_filter(word)]
  random_number = int(random.random() * len(words))
  return words[random_number].strip().lower()

def is_game_done(guessed_letters, word, word_displayed):
  return too_many_guesses(guessed_letters) or guessed_word(word, word_displayed)

def too_many_guesses(guessed_letters):
  return len(guessed_letters) >= config.GUESSES

def remaining_guesses(guessed_letters):
  return config.GUESSES - len(guessed_letters) 

def guessed_word(word, word_displayed):
  return word == ''.join(word_displayed)

def format_displayed_word(word_displayed):
  return ' '.join(word_displayed)

def print_message(message):
  print
  print '=' * 40
  print message
  print '=' * 40

def valid_guess(letter):
  if letter == '':
    print_message("Ahem, a letter would be helpful")
    return False

  if len(letter) > 1:
    print_message("Just one letter per guess please")
    return False

  if letter not in string.ascii_lowercase:
    print_message("Only lowercase letters please")
    return False

  if letter in guessed_letters or letter in word_displayed:
    print_message("Whoops, you already guessed %s" % letter)
    return False

  return True

def word_length(word):
  # TODO Strip out spaces before calculating the length
  return len(word)

guessed_letters = []
remaining_letters = list(string.ascii_lowercase)

word = pick_word()
debug("Shhh, the word is %s" % word)
print("The word has %d letters\n" % word_length(word))
word_displayed = list('_' * len(word))

while not is_game_done(guessed_letters, word, word_displayed):
  print "\n%s\t\tIncorrect guesses: %s" % (format_displayed_word(word_displayed), ''.join(guessed_letters))
  print "%s\t\tRemaining letters: %s\n" % ('  ' * (len(word) - 1), ''.join(remaining_letters))

  letter = raw_input("Guess a letter (%d left): " % remaining_guesses(guessed_letters))

  if not valid_guess(letter):
    continue

  remaining_letters.remove(letter)

  if letter in word:
    for i in range(0, len(word)):
      if word[i] == letter:
        word_displayed[i] = letter 
  else:
    guessed_letters.append(letter)


if too_many_guesses(guessed_letters):
  print_message("Sorry, you're out of guesses")
  print "The word was: %s" % word
  print "   |"
  print "   |"
  print "   O"
  print "  /|\\"
  print "   |"
  print " _/ \\_"

if guessed_word(word, word_displayed):
  print("\n%s - You guessed it!" % word)

