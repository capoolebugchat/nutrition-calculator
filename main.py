from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from typing import List, Dict
from time import time
from calculators import _tdee_calculate, _bmr_calculate, test_run

class UserData(BaseModel):
    name: str
    age: int
    sex: str
    weight: int
    height: int
    excercising_factor: float

# metadata of the APIs
tags_metadata = [
    {
        "name": "check-status",
        "description": "Check the status of the service"

    },
    {
        "name": "bmr-calculate",
        "description": "Calculate the user's BMR (recommended daily calories intake)"
    },
    {
        "name": "tdee-calculate",
        "description": "Calculation of user's daily macro intake"
    }
]

# init app with exposing RESTAPI
app = FastAPI(openapi_tags=tags_metadata)


@app.get("/", tags=["check-status"], status_code=status.HTTP_200_OK)
def check_status(response: Response):
    _status, message = test_run()
    if _status == 1:
        return {'API Calories Index Calculator': {'Status': message}}
    elif _status == 0:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {'API Calories Index Calculator': {'Status': message}}

# BMR calculator API call:
@app.post("/bmr-calculate", tags=["bmr-calculate"], status_code=status.HTTP_200_OK)
async def bmr_calculate(user_data: UserData):
    
    bmr_index = _bmr_calculate(user_data)
    res = {"name": user_data.name, "bmr_index": bmr_index}

    return res

# TDEE calculator API call
@app.post("/tdee-calculate", tags=["tdee-calculate"], status_code=status.HTTP_200_OK)
async def tdee_calculate(user_data: UserData):
    
    tdee_index = _tdee_calculate(user_data)
    res = {"name": user_data.name, "tdee_index": tdee_index}
    
    return res