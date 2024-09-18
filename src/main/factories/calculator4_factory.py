from src.calculators.calculator_4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler


def calculator4_factory():
    calc = Calculator4(NumpyHandler())
    return calc
