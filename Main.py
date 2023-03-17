import random
from BagOfWords import BagOfWords
import TextProcessing
import DataProcessing
import Brain


_BagOfWords = BagOfWords()

# Step 1 : We process all the data we have 
for N in range(2, 6):
    print(f'Data processing for N={N} started!')
    DataProcessing.ProcessAllData(_BagOfWords, N)
    print(f'Data processing for N={N} finished!')
    print("=" * 128)

# Step 2 : We now clean the back
print('Bag cleaning start!')
DataProcessing.CleanBag(_BagOfWords)
print('Bag cleaning finished!')
print("=" * 128)

# Prompt part
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


