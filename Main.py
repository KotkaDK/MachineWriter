import random
from BagOfWords import BagOfWords
import TextProcessing
import DataProcessing
import Brain
from datetime import datetime
import gc


_BagOfWords = BagOfWords()

# Step 0 : Enable garbage collection
gc.enable()

# Step 1 : We process all the data we have 
for N in range(2, 6):
    print(f'Data processing for N={N} started! [{datetime.now().strftime("%H.%M:%S %d/%m/%Y")}]')
    DataProcessing.ProcessAllData(_BagOfWords, N)
    gc.collect()
    print(f'Data processing for N={N} finished! [{datetime.now().strftime("%H.%M:%S %d/%m/%Y")}]')
    print("=" * 128)

# Step 2 : Clean the bag
print(f'Bag cleaning started! [{datetime.now().strftime("%H.%M:%S %d/%m/%Y")}]')
DataProcessing.CleanBag(_BagOfWords)
gc.collect()
print(f'Bag cleaning finished! [{datetime.now().strftime("%H.%M:%S %d/%m/%Y")}]')
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


