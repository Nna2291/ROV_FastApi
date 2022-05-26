from pydantic import BaseModel
import json


class Telemetry(BaseModel):
    light: int
