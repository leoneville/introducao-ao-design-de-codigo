from typing import Dict, List

from pytest import raises

from src.calculators.calculator_4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler:
    def average(self, numbers: List[float]) -> float:
        return 5.0


def test_calculate_integration():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
    calculator_4 = Calculator4(NumpyHandler())
    formatted_response = calculator_4.calculate(mock_request)

    assert isinstance(formatted_response, dict)
    assert formatted_response == {"data": {"Calculator": 4, "result": 2.69}}


def test_calculate():
    mock_request = MockRequest({"numbers": [5.0, 5.0, 5.0, 5.0, 5.0]})
    calculator_4 = Calculator4(MockDriverHandler())
    formatted_response = calculator_4.calculate(mock_request)

    assert isinstance(formatted_response, dict)
    assert formatted_response == {"data": {"Calculator": 4, "result": 5.0}}


def test_calculate_with_body_error():
    mock_request = MockRequest({"numbers": 2.0})
    calculator_4 = Calculator4(MockDriverHandler())

    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)

    assert str(excinfo.value) == "Body mal formatado!"
