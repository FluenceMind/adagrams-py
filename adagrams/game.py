from random import randint

LETTER_POOL = {
    "A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2,
    "G": 3, "H": 2, "I": 9, "J": 1, "K": 1, "L": 4,
    "M": 2, "N": 6, "O": 8, "P": 2, "Q": 1, "R": 6,
    "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1,
    "Y": 2, "Z": 1,
}

SCORE_CHART = {
    "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
    "D": 2, "G": 2,
    "B": 3, "C": 3, "M": 3, "P": 3,
    "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
    "K": 5,
    "J": 8, "X": 8,
    "Q": 10, "Z": 10,
}

def draw_letters():
    tiles = []
    for letter in LETTER_POOL:
        count = LETTER_POOL[letter]
        i = 0
        while i < count:
            tiles.append(letter)
            i += 1

    hand = []
    picks = 0
    while picks < 10:
        idx = randint(0, len(tiles) - 1)
        hand.append(tiles.pop(idx))
        picks += 1

    return hand

def uses_available_letters(word, letter_bank):
    word = word.upper()
    
    for char in word:
        count_word = 0
        count_bank = 0

    
        i = 0
        while i < len(word):
            if word[i] == char:
                count_word += 1
            i += 1

        j = 0
        while j < len(letter_bank):
            if letter_bank[j] == char:
                count_bank += 1
            j += 1
        
        if count_word > count_bank:
            return False

    return True

def score_word(word):
    word = word.upper()
    score = 0

    i = 0
    while i < len(word):
        ch = word[i]
        if ch in SCORE_CHART:
            score += SCORE_CHART[ch]
        i += 1

    if 7 <= len(word) <= 10:
        score += 8

    return score

def get_highest_word_score(word_list):
    best_word = word_list[0]
    best_score = score_word(best_word)

    i = 1
    while i < len(word_list):
        word = word_list[i]
        score = score_word(word)

        if score > best_score:
            best_word = word
            best_score = score
        elif score == best_score:
            if len(word) == 10 and len(best_word) != 10:
                best_word = word
                best_score = score
            elif len(word) < len(best_word) and len(best_word) != 10:
                best_word = word
                best_score = score
        i += 1

    return (best_word, best_score)