"""Addition Class"""
from calc.calculations.calculation import Calculation

class Addition(Calculation):
    """The Addition Class- Created so that we can call this class in our test program """
    def get_result(self):
        """get the addition results after calculation"""
        sum_values = 0.0
        for value in self.values:
            sum_of_values = value +  sum_values
        return sum_of_values
