from pydantic import BaseModel


class EngineCommand(BaseModel):
    pin_1: int
    pin_2: int
    speed: int
