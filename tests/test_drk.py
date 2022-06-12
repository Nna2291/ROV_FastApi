import time
from typing import List
from urllib.parse import urljoin

import pytest
import requests

from models.Engine import Engine
from models.validate.engine_command import EngineCommand


class CustomSession(requests.Session):
    def __init__(self, base_url: str):
        super().__init__()
        self.base_url = base_url

    def request(self, method, url, *args, **kwargs):
        url = urljoin(self.base_url, url)
        return super(CustomSession, self).request(method, url, *args, **kwargs)


client = CustomSession('http://raspberrypi.local:8000/')

engine_1 = Engine(pin_1=26, pin_2=27, pin_3=4)
engine_2 = Engine(pin_1=22, pin_2=23, pin_3=2)
engine_3 = Engine(pin_1=24, pin_2=25, pin_3=3)
engine_4 = Engine(pin_1=28, pin_2=29, pin_3=5)
engine_5 = Engine(pin_1=30, pin_2=31, pin_3=6)
engine_6 = Engine(pin_1=32, pin_2=33, pin_3=7)

i = 127


def launch(command_first, command_second):
    req1 = client.post('/engines', json=command_first)
    req2 = client.post('/engines', json=command_second)
    assert req1.text == req2.text
    time.sleep(15)
    command_first['speed'] = 0
    command_second['speed'] = 0
    req1 = client.post('/engines', json=command_first)
    req2 = client.post('/engines', json=command_second)
    assert req1.text == req2.text


def test_all():
    req1 = client.post('/engines', json=engine_1.get_command(i))
    req2 = client.post('/engines', json=engine_2.get_command(i))
    req3 = client.post('/engines', json=engine_3.get_command(i))
    req4 = client.post('/engines', json=engine_4.get_command(i))
    req5 = client.post('/engines', json=engine_5.get_command(i))
    req6 = client.post('/engines', json=engine_6.get_command(i))
    time.sleep(30)
    req1 = client.post('/engines', json=engine_1.get_command(0))
    req2 = client.post('/engines', json=engine_2.get_command(0))
    req3 = client.post('/engines', json=engine_3.get_command(0))
    req4 = client.post('/engines', json=engine_4.get_command(0))
    req5 = client.post('/engines', json=engine_5.get_command(0))
    req6 = client.post('/engines', json=engine_6.get_command(0))


def test_up():
    en1, en2 = engine_5, engine_6
    command_first = en1.get_command(i, reverse=True)
    command_second = en2.get_command(i)
    launch(command_first, command_second)


def test_down():
    en1, en2 = engine_5, engine_6
    command_first = en1.get_command(i)
    command_second = en2.get_command(i, reverse=True)
    launch(command_first, command_second)


def test_march():
    en1, en2 = engine_2, engine_3
    command_first = en1.get_command(i, reverse=True)
    command_second = en2.get_command(i)
    launch(command_first, command_second)


def test_march_reverse():
    en1, en2 = engine_1, engine_4
    command_first = en1.get_command(i, reverse=True)
    command_second = en2.get_command(i)
    launch(command_first, command_second)


def test_lag_left():
    en1, en2 = engine_1, engine_2
    command_first = en1.get_command(i)
    command_second = en2.get_command(i)
    launch(command_first, command_second)


def test_lag_right():
    en1, en2 = engine_3, engine_4
    command_first = en1.get_command(i)
    command_second = en2.get_command(i)
    launch(command_first, command_second)


def test_kurs_right():
    en1, en2 = engine_2, engine_4
    command_first = en1.get_command(i)
    command_second = en2.get_command(i, reverse=True)
    launch(command_first, command_second)


def test_kurs_left():
    en1, en2 = engine_1, engine_3
    command_first = en1.get_command(i)
    command_second = en2.get_command(i, reverse=True)
    launch(command_first, command_second)


def test_kren_right():
    en1, en2 = engine_6, engine_5
    command_first = en1.get_command(i, reverse=True)
    command_second = en2.get_command(i, reverse=True)
    launch(command_first, command_second)


def test_kren_left():
    en1, en2 = engine_6, engine_5
    command_first = en1.get_command(i)
    command_second = en2.get_command(i)
    launch(command_first, command_second)
