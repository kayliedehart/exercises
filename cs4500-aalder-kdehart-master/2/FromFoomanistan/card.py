class Card:
    """
    To represent a card in the game
    """
    def __init__(self, number, bull):
        """
        :param number: Int, where 1 <= number <= 104 and unique
        :param bull: Int, where 2 <= bull <= 7
        :return: Card
        """
        self.number = number
        self.bull = bull

    def __str__(self):
        return str([self.number, self.bull])


