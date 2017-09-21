
class Word(object):

    MAX_SCORE = 4
    MIN_SCORE = -4

    def __init__(self, word, definition):

        self.word = word
        self.definition = definition
        self.score = 0

    def set_score(self, score):
        self.score = int(score)

    def get_score_str(self):
        return "%s\t%s\n" % (self.word, self.score)

    def is_learned(self):
        return self.score == Word.MAX_SCORE

    def update_correct(self):
        self.score = min(self.score + 1, Word.MAX_SCORE)

    def update_wrong(self):
        self.score = max(self.score - 1, Word.MIN_SCORE)