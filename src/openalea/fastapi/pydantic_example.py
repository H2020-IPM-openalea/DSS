
from pydantic import BaseModel, Field

class ConfigParameters(BaseModel):
    timeZone: str
    timeStart: str
    timeEnd: str


class LocationWeatherDatum(BaseModel):
    longitude: float
    latitude: float
    altitude: float
    data: list[list[float]]
    length: int
    width: int


class WeatherData(BaseModel):
    timeStart: str
    timeEnd: str
    interval: int
    weatherParameters: list[int]
    locationWeatherData: list[LocationWeatherDatum]


class input_schema(BaseModel):
    modelId: str
    configParameters: ConfigParameters
    weatherData: WeatherData