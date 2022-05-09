from fastapi import FastAPI
from models.engine_command import EngineCommand

app = FastAPI()


@app.get("/")
async def root():
    """
    Classic hello world function.

    :return: JSON
    """
    return {"message": "Hello World"}


@app.post("/engines")
async def engine_command(command: EngineCommand):
    return {'Successfully turn on engine': {
        'pin_1': command.pin_1,
        'pin_2': command.pin_2,
        'speed': command.speed
    }}
