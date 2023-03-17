import os
import math
import TextProcessing
from BagOfWords import BagOfWords


def GetTextFiles() -> list[str]:
    """
    Get all the text files
    :return: All text file names in data directory
    """

    # Step 1 : Loop over all files in directory
    Files = []
    for FileName in os.listdir("./Data"):
        if FileName.endswith('.txt'):
            # Step 2 : Add file name to files, if it's a .txt file
            Files.append(FileName)

    # Step 3 : Return the files
    return Files


def ProcessAllData(Bag: BagOfWords, N):
    """
    Process all the data from the "Data" folder
    :return: All tokens from each text in the "Data" folder
    """

    # Step 1 : Get all file names
    Files = GetTextFiles()

    # Step 2 : Process individual files
    for File in Files:
        Tokens = TextProcessing.ProcessText(f'./data/{File}')
        TextProcessing.AddWordsToDictionary(Bag, Tokens, N)


def SlidingWindowMatrix(Tokens: list[any], WindowSize: int) -> list[list[any]]:
    """
    Creates sliding window sequences for better context
    :param Tokens: The words we want to make the sequences of
    :param WindowSize: The size of the windows
    :return: The matrix
    """

    # Step 1 : Loop over the tokens
    Matrix = []
    for i in range(len(Tokens) - (WindowSize - 1)):
        Matrix.append(Tokens[i:WindowSize + i])

    # Step 2 : Return the matrix
    return Matrix


def SequenceToMLMatrix(Sequence: list[int], Inputs: int, FillerValue: int) -> list[list[int]]:
    """
    Converts a number sequence to a Neural Network ready Matrix
    :param Sequence: A list of number inputs
    :param Inputs: The amount of input nodes in your Neural Network
    :param FillerValue: The no-meaning value to fill empty slots
    :return: The Neural Network ready Matrix
    """

    # Step 1 : Count rows needed
    Rows = math.ceil(len(Sequence) / Inputs)

    # Step 2 : Count total values based on rows and inputs
    TotalValues = Rows * Inputs

    # Step 3 : Add values so len(Sequence) == TotalValues
    if len(Sequence) < TotalValues:
        Sequence.extend([FillerValue] * (TotalValues - len(Sequence)))

    # Step 4 : Convert the list into a matrix
    # x = Inputs, y = Rows
    Matrix = [Sequence[i:i+Inputs] for i in range(0, len(Sequence), Inputs)]

    # Step 5 : Return the matrix
    return Matrix


def NGram(Tokens: list[str], N: int) -> list[str]:

    # Too short token list or too small N value
    if len(Tokens) < N-1 or N < 2:
        # Return empty
        return []

    # No need to do more logic than necessary
    if N == 2:
        return Tokens

    # N-Grams
    NGrams = []

    # The loop that takes Length and N into account
    for i in range(len(Tokens) - (N - 2)):
        # Slice the N-Gram we want
        NGramSlice = Tokens[i:i+N-1]

        # Append the N-Gram slice to the list
        NGrams.append(" ".join(NGramSlice))

    # Return the N-Grams
    return NGrams


def CleanBag(Bag: BagOfWords):
    # Step 1 : Loop over all keys in the dictionary
    for Entry in Bag.BoW:

        # Step 2 : Find the highest value in the post-word dictionary
        HighestValue = max(Bag.BoW[Entry].values())

        # Step 3 : Remove all post-words that are less than the highest value
        Bag.BoW[Entry] = {E: V for E, V in Bag.BoW[Entry].items() if V == HighestValue}

        # Step 4 : Check for the length of each post-word dictionary
        if len(Bag.BoW[Entry].items()) == 1:
            # Convert dictionary to string
            Bag.BoW[Entry] = list(Bag.BoW[Entry].keys())
        else:
            # Convert dictionary to string based on the first key
            Bag.BoW[Entry] = list(Bag.BoW[Entry].keys())[0]