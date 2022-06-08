from pydantic import BaseModel
import json
from typing import Union


class EngineCommand(BaseModel):
    pin_1: int
    pin_2: int
    pin_3: int
    speed: int

    def __str__(self):
        dict_ = {'task': 'POST', 'pin_1': self.pin_1, 'pin_2': self.pin_2, 'pin_3': self.pin_3, 'speed': self.speed}
        result = json.dumps(dict_)
        return result


