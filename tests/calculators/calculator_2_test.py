from typing import Dict, List

from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_2 import Calculator_2


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        return 3


# Integração entre NumpyHandler e Calculator2
def test_calculate_integration():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
    calculator_2 = Calculator_2(NumpyHandler())
    formatted_response = calculator_2.calculate(mock_request)

    assert isinstance(formatted_response, dict)
    assert formatted_response == {"data": {"Calculator": 2, "result": 0.08}}


def test_calculate():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
    driver = MockDriverHandler()
    calculator_2 = Calculator_2(driver)
    formatted_response = calculator_2.calculate(mock_request)

    assert isinstance(formatted_response, dict)
    assert formatted_response == {"data": {"Calculator": 2, "result": 0.33}}
