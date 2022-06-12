import serial
from fastapi import FastAPI, HTTPException
from serial.serialutil import SerialException

from models.validate.engine_command import EngineCommand
from models.validate.telemetry import Telemetry

app = FastAPI()

ports = ['/dev/ttyUSB1', '/dev/ttyUSB0']

for port in ports:
    try:
        ser = serial.Serial(port, 9600, timeout=2)
        break
    except SerialException:
        ser = None


@app.get("/")
async def root():
    """
    Classic hello world function.

    :return: JSON
    """
    return {"message": "Hello World"}


@app.get("/data")
async def data():
    if ser is None:
        return HTTPException(status_code=500, detail="Arduino is not connected")
    ser.write('{"task": "GET"}'.encode())
    json_raw = ser.readline().decode('utf-8').rstrip()
    return dict(Telemetry.parse_raw(json_raw))


@app.post("/engines")
async def engine_command(command: EngineCommand):
    if ser is None:
        return HTTPException(status_code=500, detail="Arduino is not connected")
    ser.write(str.encode(str(command)))
    return 'ok'
