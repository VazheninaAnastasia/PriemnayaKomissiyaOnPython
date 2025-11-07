class Calculator:
    # empty constructor
    def __init__(self):
        pass

    # add method - given two numbers, return the addition
    def add(self, x1, x2):
       """ given two numbers, return the addition
       :param x1:
       :param x2:
       :return:
       """
       return x1 + x2

    # multiply method - given two numbers, return the
    # multiplication of the two
    def multiply(self, x1, x2):
        """given two numbers, return the multiplication of the two
        :param self:
        :param x1:
        :param x2:
        :return:
        """
        return x1 * x2

    # subtract method - given two numbers, return the value
    # of first value minus the second
    def subtract(self, x1, x2):
        """given two numbers, return the value of first value minus the second

        :param x1:
        :param x2:
        :return:
        """
        return x1 - x2

    # divide method - given two numbers, return the value
    # of first value divided by the second
    def divide(self, x1, x2):
        """given two numbers, return the value of first value divided by the second
        :param x1:
        :param x2:
        :return:
        """
        if x2 != 0:
            return x1 / x2
