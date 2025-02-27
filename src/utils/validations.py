from src.model.exceptions import ForbiddenException


def authorize_user(current_id: int, id: int) -> None:
    if current_id != id:
        raise ForbiddenException(
            detail='User not allowed to acces/use this resource.'
        )
