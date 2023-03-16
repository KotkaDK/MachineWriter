import random
from BagOfWords import BagOfWords
import TextProcessing
import DataProcessing


def Predict(Text: str, _BagOfWords: BagOfWords) -> str:

    # Step 1 : Tokenize the input
    Tokens = TextProcessing.Tokenize(Text)


