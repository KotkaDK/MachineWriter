import random
from BagOfWords import BagOfWords
import TextProcessing
import DataProcessing
import Brain


_BagOfWords = BagOfWords()

for N in range(2, 6):
    DataProcessing.ProcessAllData(_BagOfWords, N)

prompt = input("Enter prompt: ")
prompt = Brain.PredictSequence(prompt, _BagOfWords, 20)
print(prompt)
print("=" * 128)

while True:
    prompt = input("Enter prompt: ")
    prompt = Brain.PredictSequence(prompt, _BagOfWords, 20)
    print(prompt)
    print("=" * 128)