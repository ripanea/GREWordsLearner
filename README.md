# GREWordsLearner

GREWordsLearner is a small command-line quiz app that helps users learn the list of words necessary for the GRE vocabulary.

## How it works?

The app repeatedly asks the user to select the correct definition for a word from five provided definitions. 
Each word has a score that is influenced by the user's answers. A correct answer increases the word's score with +1, while
 a wrong answer decreases the word's score with -1. The minimum score a word can have is -4, while the maximum score is +4.
A word is considered 'mastered' if its score reaches the maximum score (+4). When a word is mastered, the user will not be
quizzed about it anymore.

The aim of the quiz is to 'master' all words, by selecting the correct definition every time.

Progress will be saved at the end of each session, as each user has a 'profile' that keeps track of the word scores.

## Getting started

### Pre-requisites

This app requires Python 2.7. 

### Installation and Usage

No installation required. Just clone and run. Create a new profile when prompted and start learning!

    git clone https://github.com/ripanea/GREWordsLearner.git
    ./Main.py

## Authors

Razvan Panea


