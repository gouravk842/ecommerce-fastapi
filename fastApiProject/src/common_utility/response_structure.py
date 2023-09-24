from starlette import status
from starlette.responses import Response, JSONResponse


def send_response(
        data=None,
        status_code: int = status.HTTP_200_OK,
        error=None,
) -> JSONResponse:
    response = {
        "error": error,
        "data": data,
    }

    return JSONResponse(response, status_code=status_code)
