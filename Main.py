import random

from BagOfWords import BagOfWords
import TextProcessing
import DataProcessing
import Brain


_BagOfWords = BagOfWords()

# We now process all the data
DataProcessing.ProcessAllData(_BagOfWords)

"""
for word in _BagOfWords.BoW.keys():
    print(f'{word} : {_BagOfWords.GetPostWords(word)}')
"""

prompt = random.choice(list(_BagOfWords.BoW.keys()))
count = random.randint(1, 20)
prompt = Brain.PredictSequenceNoContext(prompt, count, _BagOfWords)
print(prompt)
