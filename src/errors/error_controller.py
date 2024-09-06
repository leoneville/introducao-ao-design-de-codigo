from typing import Dict

from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


def handle_errors(error: Exception) -> Dict:
    if isinstance(error, (HttpUnprocessableEntityError, HttpBadRequestError)):
        return {
            "status_code": error.status_code,
            "body": {"errors": [{"title": error.name, "detail": error.message}]},
        }

    return {
        "status_code": 500,
        "body": {"errors": [{"title": "Server Error", "detail": str(error)}]},
    }
