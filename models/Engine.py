import json


class Engine:
    def __init__(self, pin_1: int, pin_2: int, pin_3: int):
        self.pin_1 = pin_1
        self.pin_2 = pin_2
        self.pin_3 = pin_3

    def get_command(self, speed: int, reverse=False) -> dict:
        if reverse:
            pin_1, pin_2, pin_3 = self.pin_2, self.pin_1, self.pin_3
        else:
            pin_1, pin_2, pin_3 = self.pin_1, self.pin_2, self.pin_3
        json = {'task': 'POST', 'pin_1': pin_1, 'pin_2': pin_2, 'pin_3': pin_3, 'speed': speed}
        return json

    def off(self) -> dict:
        json = {'task': 'POST', 'pin_1': self.pin_1, 'pin_2': self.pin_2, 'pin_3': self.pin_3, 'speed': 0}
        return json
