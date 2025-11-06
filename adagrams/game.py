from random import randint

LETTER_POOL = {
    "A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2,
    "G": 3, "H": 2, "I": 9, "J": 1, "K": 1, "L": 4,
    "M": 2, "N": 6, "O": 8, "P": 2, "Q": 1, "R": 6,
    "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1,
    "Y": 2, "Z": 1,
}

SCORE_CHART = {
    "A": 1, "E": 1, "I": 1, "O": 1, "U": 1,
    "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
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
        for _ in range(count):
            tiles.append(letter)

    hand = []
    for _ in range(10):
        idx = randint(0, len(tiles) - 1)
        hand.append(tiles[idx])
        tiles[idx] = tiles[-1]
        tiles.pop()

    return hand

def uses_available_letters(word, letter_bank):
    bank_counts = {}
    for letter in letter_bank:
        upper_letter = letter.upper()
        if upper_letter in bank_counts:
            bank_counts[upper_letter] += 1
        else:
            bank_counts[upper_letter] = 1

    for ch in word.upper():
        if ch in bank_counts and bank_counts[ch] > 0:
            bank_counts[ch] -= 1
        else:
            return False
    return True

def score_word(word):
    total_score = 0
    for ch in word.upper():
        if ch in SCORE_CHART:
            total_score += SCORE_CHART[ch]

    word_len = len(word)
    if 7 <= word_len <= 10:
        total_score += 8

    return total_score

def get_highest_word_score(word_list):
    highest_score = 0
    for word in word_list:
        points = score_word(word)
        if points > highest_score:
            highest_score = points

    candidates = []
    for word in word_list:
        if score_word(word) == highest_score:
            candidates.append(word)

    for word in candidates:
        if len(word) == 10:
            return (word, highest_score)

    best_word = candidates[0]
    best_len = len(best_word)
    for i in range(1, len(candidates)):
        w = candidates[i]
        wl = len(w)
        if wl < best_len:
            best_word = w
            best_len = wl

    return (best_word, highest_score)