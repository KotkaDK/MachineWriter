import random
from BagOfWords import BagOfWords
import TextProcessing
import DataProcessing


def Predict(Text: str, _BagOfWords: BagOfWords) -> str:

    # Step 1 : Tokenize the input
    Tokens = TextProcessing.Tokenize(Text)

    # Step 2 : Get the N-Grams of the tokens
    NGrams = [
        DataProcessing.NGram(Tokens, 5),
        DataProcessing.NGram(Tokens, 4),
        DataProcessing.NGram(Tokens, 3),
        DataProcessing.NGram(Tokens, 2)
    ]

    # Step 3 : Get the last N-Gram of each window
    LastNGrams = []
    for NGram in NGrams:
        if len(NGram) > 0:
            LastNGrams.append(NGram[-1])
    print(LastNGrams)

    # Step 4 : Get the first dictionary match
    DictionaryMatch = None
    for NGram in LastNGrams:
        if NGram in _BagOfWords.BoW:
            DictionaryMatch = NGram
            break

    # Step 5 : Check if we have no match
    if DictionaryMatch is None:
        return ""

    # Step 6 : Find the best post-word match (the most frequent post-word)
    PostWordMatch = _BagOfWords.GetMostProbablePostWord(DictionaryMatch)

    # Step 7 : Return the best post-word match
    return PostWordMatch


def PredictSequence(Text: str, _BagOfWords: BagOfWords, Count: int) -> str:
    NewText = " ".join(TextProcessing.Tokenize(Text))

    for i in range(Count):
        Word = Predict(NewText, _BagOfWords)
        if Word != "":
            NewText = f'{NewText} {Word}'
        else:
            break

    return NewText

