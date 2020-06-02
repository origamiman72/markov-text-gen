import numpy as np

# Resources used: towardsdatascience.com

source = open('source.txt', encoding = 'utf8').read()

words = source.split()

# Generator to reproduce pairs from the text
def make_pairs(text):
    for i in range(len(text) - 1):
        yield (text[i], text[i + 1])

pairs = make_pairs(words)

word_dict = {}

for w1, w2 in pairs:
    if w1.lower() in word_dict.keys():
        word_dict[w1.lower()].append(w2)
    else:
        word_dict[w1.lower()] = [w2]

def generate_sentence(start = None, length = 10):
    if start == None:
        start = np.random.choice(words)
        while start.islower():
            start = np.random.choice(words)
    chain = [start]
    curr = 1
    while curr < length: # or chain[-1][-1] not in [".", "!", "?"]:
        try:
            chain.append(np.random.choice(word_dict[chain[-1].lower()]))
        except:
            chain.append(np.random.choice(words))
        curr += 1
    return ' '.join(chain)