import random
from BagOfWords import BagOfWords
import TextProcessing
import DataProcessing
import Brain


_BagOfWords = BagOfWords()

for N in range(2, 6):
    DataProcessing.ProcessAllData(_BagOfWords, N)

prompt = input("Enter prompt: ")
count = int(input("Enter amount of words to add: "))
prompt = Brain.PredictSequence(prompt, _BagOfWords, count)
print(prompt)
print("=" * 128)

while True:
    prompt = input("Enter prompt: ")
    count = int(input("Enter amount of words to add: "))
    prompt = Brain.PredictSequence(prompt, _BagOfWords, count)
    print(prompt)
    print("=" * 128)