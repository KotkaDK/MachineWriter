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


def ProcessAllData(Bag: BagOfWords):
    """
    Process all the data from the "Data" folder
    :return: All tokens from each text in the "Data" folder
    """

    # Step 1 : Get all file names
    Files = GetTextFiles()

    # Step 2 : Process individual files
    for File in Files:
        Tokens = TextProcessing.ProcessText(f'./data/{File}')
        TextProcessing.AddWordsToDictionary(Bag, Tokens)


def SlidingWindowMatrix(Tokens: list[any]) -> list[list[any]]:
    """
    Creates sliding window sequences for better context
    :param Tokens: The words we want to make the sequences of
    :return: The matrix
    """

    # Step 1 : Loop over the tokens
    WindowSize = 2
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