import random
from BagOfWords import BagOfWords
import TextProcessing
import DataProcessing
import Brain


prompt = "the cat sat on the"
tokens = TextProcessing.Tokenize(prompt)
N_Grams = DataProcessing.NGram(tokens, 3)
print(tokens)
print(N_Grams)