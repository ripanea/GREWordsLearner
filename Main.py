#!/usr/bin/python2.7

import random
import os

from Word import Word

print("Welcome to GRE Word Learner!\n\n")

# Initialize the main words dictionary
words = {}

# Read the word definitions from file
with open("words.dat") as inp:
    for line in inp:
        word, definition = line.strip("\r\n").split("\t", 1)

        words[word] = Word(word, definition)

# Identify which user is learning
msg = "Please state your name to read your profile!\nIf you do not have a profile yet, just specify your name for a new profile: "
username = str(raw_input(msg)).lower()

# Check if the username is one string
if not username.isalnum():
    print("Profile name must be only alphanumeric (i.e. contains only letters and digits). Please provide a new username!")

# Check if the file exists
if os.path.exists("profiles/%s.prof" % username):
    print("Profile '%s' found! Now loading your profile.\n\n" % username)

    # Initialize the scores
    with open("profiles/%s.prof" % username) as inp:
        for line in inp:
            word, score = line.strip("\r\n").split("\t", 1)

            words[word].set_score(score)

else:
    print("Profile '%s' not found! Creating a new profile with that name.\n\n" % username)

# Separate the words into completely learned words and to learn words
to_learn = {}
complete = {}
for word, word_obj in words.iteritems():
    if word_obj.is_learned():
        complete[word] = word_obj
    else:
        to_learn[word] = word_obj

# Check if the list of words is exhausted
if not to_learn:
    print("All words have been mastered! You can create a new profile and start from scratch.")
    exit(1)

# Initialize the game statistics
correct_count = 0
wrong_count = 0

# Start the quiz
stop = False
while not stop:

    # Randomly obtain a new word to quiz
    main_word = random.choice(to_learn.keys())

    # Randomly select 4 alternative words that are not the main word
    alt_words = []
    while len(alt_words) != 4:
        new_word = random.choice(words.keys())

        # Check if word was already selected
        if new_word not in alt_words:
            alt_words.append(new_word)

    # Collect all definitions and shuffle to list
    definitions = [ words[main_word].definition ]
    definitions.extend( [ words[alt_word].definition for alt_word in alt_words ] )
    random.shuffle(definitions)

    # Obtain the correct answer
    main_definition_idx = definitions.index(words[main_word].definition)

    # Quiz the word
    print("The word is: %s. Please choose a definition." % main_word.upper())
    for i, definition in enumerate(definitions):
        print("    %d -  %s" % (i+1, definition))

    # Obtain a valid response
    valid = False
    while not valid:

        # Obtain the response
        response = str(raw_input("\nYour answer is: ")).lower()

        # Check if the response is to quit
        if response == "q":
            valid = True
            stop = True

        # Check if the response is a digit
        elif response.isdigit():
            val = int(response)

            # Check if the digit is in the correct range
            if val in range(1,6):

                # This is a valid answer
                valid = True

                # Check if the answer is the correct answer
                if val == main_definition_idx + 1:
                    print("CORRECT!\n")

                    # Increment the number of correct answers
                    correct_count += 1

                    # Increase the word score
                    words[main_word].update_correct()
                else:
                    print("WRONG!\n")

                    # Increment the number of wrong answers
                    wrong_count += 1

                    # Decrease the word score
                    words[main_word].update_wrong()

                # Print the definition of the word
                print("%s - %s\n\n" % (main_word.upper(), words[main_word].definition))

                # Check if the word is learned. If learned, remove from to_learn and add to complete
                if words[main_word].is_learned():
                    del to_learn[main_word]
                    complete[main_word] = words[main_word]

        # Return answer types is no valid answer was provided
        if not valid:
            print("Please provide only a number between 1 and 5, which represents the definition that you "
                  "believe is correct. To quit the program, type 'q'.")

# Print The final result
print("""
FINAL RESULTS:
  Correct answers this session: %d
  Wrong answers this session: %d
  Total words mastered (maximum score achieved): %d / %d (%.2f%%)
""" % (correct_count, wrong_count, len(complete), len(words), len(complete)*100.0/len(words)) )

# Save the ratings in the user file
with open("profiles/%s.prof" % username, "w") as out:
    for word, word_obj in words.iteritems():
        out.write(word_obj.get_score_str())