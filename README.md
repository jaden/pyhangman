# Simple Hangman Game

Reads a random lowercase word from a word list (usually found in `/usr/share/dict/words` on Linux and Mac) and prompts the user to guess a letter until the word is guessed or the maximum number of guesses is reached.

## Dependencies

Python 2.x or 3.x

## Configuration

At the top of the Python file there's a configuration section with the following options to configure.

`WORDS_FILE` - The file containing a list of words

`GUESSES` - The number of guesses the user is allowed before they're hung

`MIN_WORD_LENGTH` - The minimum number of letters allowed in a word (used to filter out short words from the word list). Set to 0 to disable filtering by length

`DEBUG` - Set to `True` to print debugging output, including the word to be guessed

## Usage

Run `python hangman.py` and guess letters one at a time
