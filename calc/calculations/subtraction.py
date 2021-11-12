"""Subtraction Class"""
import pprint

from calc.calculations.calculation import Calculation

class Subtraction(Calculation):
    def get_result(self):
        """get the subtraction results after calculation"""
        difference_values = 0.0
        for value in self.values:
            difference_values =   difference_values - value
            print.print(value)
        return  difference_values
