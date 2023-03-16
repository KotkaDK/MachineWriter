import random
from BagOfWords import BagOfWords
import TextProcessing
import DataProcessing


def PredictWord(Text: str, _BagOfWords: BagOfWords) -> str:

    # Step 1 : Tokenize the text
    Tokens = TextProcessing.Tokenize(Text)

    # Step 2 : Find most probable post-word for each token
    PostWords = []
    for Token in Tokens:
        if Token in _BagOfWords.BoW:
            # Get the keys and values
            keys = list(_BagOfWords.BoW[Token].keys())
            values = list(_BagOfWords.BoW[Token].values())

            # Take a weighted random choice
            Word = random.choices(keys, weights=values)[0]

            # Append the word
            PostWords.append({Word: _BagOfWords.BoW[Token][Word]})
        else:
            PostWords.append({"IGNORE": -1})

    # Step 3 : Convert to sliding windows matrix
    Matrix = DataProcessing.SlidingWindowMatrix(PostWords)

    # Step 4 : Find the most probable per window
    PostWords = []
    for Window in Matrix:
        PostWords.append(max(Window, key=lambda d: list(d.values())[0]))

    # Step 5 : Find the most probable of them all
    MostProbable = list(max(PostWords, key=lambda d: list(d.values())[0]).keys())[0]

    return MostProbable


def PredictSequence(Text: str, Times: int, _BagOfWords: BagOfWords) -> str:
    # Step 1 : Predict over and over again
    for i in range(Times):
        Text = f'{Text.lower()} {PredictWord(Text, _BagOfWords)}'

    # Step 2 : Return the new text
    return Text


def PredictNoContext(Text: str, _BagOfWords: BagOfWords):
    # Step 1 : Tokenize the text
    Tokens = TextProcessing.Tokenize(Text)

    # Step 2 : Get the last token
    EndToken = Tokens[-1]

    # Step 3 : Check if it exists in the bag of words
    Word = ""
    if EndToken in _BagOfWords.BoW:
        # Get the keys and values
        keys = list(_BagOfWords.BoW[EndToken].keys())
        values = list(_BagOfWords.BoW[EndToken].values())

        # Take a weighted random choice
        Word = random.choices(keys, weights=values)[0]
    else:
        RandomToken = random.choice(list(_BagOfWords.BoW.keys()))

        # Get the keys and values
        keys = list(_BagOfWords.BoW[RandomToken].keys())
        values = list(_BagOfWords.BoW[RandomToken].values())

        # Take a weighted random choice
        Word = random.choices(keys, weights=values)[0]

    # Step 4 : Return the word
    return Word


def PredictSequenceNoContext(Text: str, Times: int, _BagOfWords: BagOfWords) -> str:
    # Step 1 : Predict over and over again
    for i in range(Times):
        Text = f'{Text.lower()} {PredictNoContext(Text, _BagOfWords)}'

    # Step 2 : Return the new text
    return Text
