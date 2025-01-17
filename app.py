from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def root():
    return {'Mesage': 'Hello world!'}
