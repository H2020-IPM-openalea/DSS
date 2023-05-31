from pathlib import Path
from datamodel_code_generator import InputFileType, generate


jsontext = """
{
  "modelId": "PSILARTEMP",
  "configParameters": {
    "timeZone": "Europe/Oslo",
    "timeStart": "2020-05-01",
    "timeEnd": "2020-05-03"
  },
  "weatherData": {
    "timeStart": "2020-04-30T22:00:00Z",
    "timeEnd": "2020-05-02T22:00:00Z",
    "interval": 86400,
    "weatherParameters": [
        1002
    ],
    "locationWeatherData": [
        {
            "longitude": 10.781989,
            "latitude": 59.660468,
            "altitude": 94.0,
            "data": [
                [
                    5.7
                ],
                [
                    8.2
                ],
                [
                    8.5
                ]
            ],
            "length": 3,
            "width": 1
        }
    ]
  }
}
"""
async def json_to_pydantic(jsonstring):
    output = Path("pydantic_input_model.py")
    generate(jsonstring, input_file_type=InputFileType.Json, output=output)




