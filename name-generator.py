import random

word_file = "words.txt"
WORDS = open(word_file).read().splitlines()
word = random.choice(WORDS) + ' ' + random.choice(WORDS) + random.choice(WORDS)
for x in range(0, 50):
    word = random.choice(WORDS) + ' ' + random.choice(WORDS) + ' ' + random.choice(WORDS)
    print word
