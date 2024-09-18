from typing import Dict, List
from flask import request as FlaskRequest

from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        calculated_average = self.__calculate_average(input_data)

        formatted_response = self.__format_response(calculated_average)
        return formatted_response

    def __validate_body(self, body: Dict) -> List[float | int]:
        if (
            "numbers" not in body
            or not isinstance(body["numbers"], list)
            or len(body["numbers"]) < 1
        ):
            raise HttpUnprocessableEntityError("Body mal formatado!")

        input_data = body["numbers"]
        return input_data

    def __calculate_average(self, input_data: List[float]) -> float:
        result = self.__driver_handler.average(input_data)
        return result

    def __format_response(self, calculated_average: float) -> Dict:
        return {"data": {"Calculator": 4, "result": round(calculated_average, 2)}}
