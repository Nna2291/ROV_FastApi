from pydantic import BaseModel
import json


class EngineCommand(BaseModel):
    pin_1: int
    pin_2: int
    speed: int

    def __str__(self):
        dict_ = {'pin_1': self.pin_1, 'pin_2': self.pin_2, 'speed': self.speed}
        result = json.dumps(dict_)
        return result
