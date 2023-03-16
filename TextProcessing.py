import re
from BagOfWords import BagOfWords


def Tokenize(ParsedText: str) -> list[str]:
    """
    Tokenizes a string
    :param ParsedText: The text you want to tokenize
    :return: Tokens based on the parsed text
    """

    # Step 1 : Lowercase the text
    ParsedText = ParsedText.lower()

    # Step 2 : Removing non-alphanumeric characters except spaces
    ParsedText = re.sub(r'[^\w\s]', '', ParsedText)

    # Step 3 : Tokenize the text
    Tokens = ParsedText.split()

    # Step 4 : Return the tokens
    return Tokens


def ProcessText(File: str) -> list[str]:
    """
    Process the content of a file
    :param File: The file we want to open and process
    :return: The tokens of the text content
    """

    # Step 1 : Open the file in read mode
    f = open(File, "r", encoding='utf-8')

    # Step 2 : Read the content of the file
    Content = f.read()

    # Step 3 : Close the file
    f.close()

    # Step 4 : Tokenize the content
    Tokens = Tokenize(Content)

    # Step 5 : Return the text
    return Tokens


def AddWordsToDictionary(Bag: BagOfWords, Tokens: list[str]):
    """
    Add words to a bag of words
    :param Bag: The bag we want to add words and post-words to
    :param Tokens: The tokens (words) we want to loop over
    :return: Nothing
    """

    # Step 1 : Loop over all the tokens
    for i, Word in enumerate(Tokens):
        # Step 2 : Add the token to the bag of words
        Bag.AddWord(Word)

        if i < len(Tokens) - 1:
            # Step 3 : Get the post-word token
            PostWord = Tokens[i + 1]

            # Step 4 : Add the post-word token to the bag of words
            Bag.AddPostWord(Word, PostWord)