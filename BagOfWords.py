

class BagOfWords:

    BoW = dict()

    # == == == == == == == == == == == == == == == == == == == == == #

    def AddWord(self, Word: str):
        """
        Add a word to the bag of words
        :param Word: the word we want to add
        :return: Nothing
        """

        # Step 1 : Check if the word doesn't exist
        if Word not in self.BoW:
            # Step 2 : Add the word with empty post-word list
            self.BoW[Word] = dict()

    # == == == == == == == == == == == == == == == == == == == == == #

    def RemoveWord(self, Word: str):
        """
        Remove a word from the bag of words
        :param Word: the word we want to remove
        :return: Nothing
        """

        # Step 1 : Check if the word exists
        if Word in self.BoW:
            # Step 2 : Delete it
            del self.BoW[Word]

    # == == == == == == == == == == == == == == == == == == == == == #

    def AddPostWord(self, Key: str, Word: str):
        """
        Add a post-word to a word
        :param Key: The word we want to add the post-word to
        :param Word: The post-word we want to add
        :return: Nothing
        """

        # Step 1a : Check if the key exists and if the post-word doesn't
        if Key in self.BoW and Word not in self.BoW[Key]:
            # Step 2a : Add the post-word to the word
            self.BoW[Key][Word] = 1
            return

        # Step 1b : Check if the key and post-word exists
        if Key in self.BoW and Word in self.BoW[Key]:
            # Step 2b : Add 1 count to the post-word
            self.BoW[Key][Word] = self.BoW[Key][Word] + 1
            return

        # Step 1c : Check if the key doesn't exist
        if Key not in self.BoW:
            # Step 2c : Add the key and post-word
            self.BoW[Key] = [Word]
            return

    # == == == == == == == == == == == == == == == == == == == == == #

    def GetPostWords(self, Key: str) -> list[str]:
        """
        Returns all the post-words associated with a specific word
        :param Key: The word we want the post-words from
        :return: post-words
        """

        # Step 1 : Check if word exists
        if Key in self.BoW:
            # Step 2 : Return post-words
            return self.BoW[Key]

    # == == == == == == == == == == == == == == == == == == == == == #

    def RemovePostWord(self, Key: str, Word: str):
        """
        Removes a post-word from a word
        :param Key: The word we want to remove the post-word from
        :param Word: The post-word we want to remove
        :return: Nothing
        """

        # Step 1 : Check if the key and post-word exists
        if Key in self.BoW and Word in self.BoW[Key]:
            # Step 2 : Remove the post-word
            del self.BoW[Key][Word]