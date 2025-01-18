from fastapi import APIRouter


router = APIRouter()


@router.get('/')
def root():
    return {'Mesage': 'Hello world!'}
