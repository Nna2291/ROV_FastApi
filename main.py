import json

import serial
from fastapi import FastAPI
from serial.serialutil import SerialException

from models.engine_command import EngineCommand

app = FastAPI()
try:
    ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=2)
except SerialException:
    # ser = serial.Serial('/dev/cu.usbserial-1410', 9600, timeout=1.5)
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)


@app.get("/")
async def root():
    """
    Classic hello world function.

    :return: JSON
    """
    return {"message": "Hello World"}


@app.get("/data")
async def data():
    dict_ = {'task': 'GET'}
    ser.write(json.dumps(dict_))
    line = ser.readline().decode('utf-8').rstrip()
    print(line)


@app.post("/engines")
async def engine_command(command: EngineCommand):
    ser.write(str.encode(str(command)))
    line = ser.readline().decode('utf-8').rstrip()
    return line
