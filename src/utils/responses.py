from http import HTTPStatus

responses={
    'bad_request': {
        HTTPStatus.BAD_REQUEST: {
            'description': 'Invalid request.',
            'content': {
                'application/json': {
                    'example': {'detail': 'Invalid data type.'}
                }
            }
        }
    },
    'internal_server_error': {
        HTTPStatus.INTERNAL_SERVER_ERROR: {
            'description': 'Internal server error.'
        }
    },
    'unauthorized': {
        HTTPStatus.UNAUTHORIZED: {
            'description': 'Invalid credentials.',
            'content': {
                'application/json': {
                    'example': {'detail': 'Invalid credentials.'}
                }
            }
        }
    },
    'not_found': {
        HTTPStatus.NOT_FOUND: {
            'description': 'Resource not found.',
            'content': {
                'application/json': {
                    'example': {'detail': 'Resource not found.'}
                }
            }
        }
    }
}
