from starlette.responses import JSONResponse


class ErrorsGenerator:

    def generate_error(self, status_code: int, msg: str):
        return JSONResponse(
            status_code=status_code,
            content={
                'error': {
                    'code': status_code,
                    'message': f'{msg}'
                }
            }
        )
