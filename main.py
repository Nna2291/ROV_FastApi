from fastapi import FastAPI
from models.engine_command import EngineCommand
import serial

app = FastAPI()
ser = serial.Serial('dev/tty/USB1', 9600, timeout=1)


def parse_to_bytes(a):
    data = f"{a}\n"
    return str.encode(data)


@app.get("/")
async def root():
    """
    Classic hello world function.

    :return: JSON
    """
    return {"message": "Hello World"}


@app.post("/engines")
async def engine_command(command: EngineCommand):
    ser.write(parse_to_bytes(command.speed))
    line = ser.readline().decode('utf-8').rstrip()
    return line
