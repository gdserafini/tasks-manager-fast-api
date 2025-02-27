from src.model.exceptions import InvalidLoginException


def authorize_user(current_id: int, id: int) -> None:
    if current_id != id:
        raise InvalidLoginException(
            detail='User not allowed to acces/use this resource.'
        )
