from fastapi import APIRouter,HTTPException
from pydantic import BaseModel  # 
from typing import Dict
import pickle
import pandas as pd
import json
#from .models.item import InputData

router = APIRouter()

class InputData(BaseModel):
    jobtitle: str
    age: int
    performance: int
    education: str
    department: str
    seniority: int
    gender: str



keys= ['jobtitle','age','performance','education','department',
       'seniority','gender']
# Post Endpoint
@router.post("/predict/")
async def predict(data: InputData):
    try:
        input_dict = data.model_dump()
        missing_keys = [key for key in keys if key not in input_dict.keys()]
        if missing_keys:
            raise KeyError(f"Missing keys: {', '.join(missing_keys)}")

        # Validating input data
        if input_dict["gender"] not in ["Female", "Male"]:
            raise ValueError("Invalid gender value. Gender must be 'Female' or 'Male'.")
        if input_dict["performance"] not in [1, 2, 3, 4, 5]:
            raise ValueError("Invalid performance value. Performance must be between 1 and 5.")
        if input_dict["jobtitle"] not in ['Graphic Designer', 'Software Engineer', 'Warehouse Associate',
                                           'IT', 'Sales Associate', 'Driver', 'Financial Analyst',
                                           'Marketing Associate', 'Data Scientist', 'Manager']:
            raise ValueError("Invalid jobtitle value.")
        if input_dict["age"] < 0 or input_dict["age"] > 100:
            raise ValueError("Invalid age value. Age must be between 0 and 100.")
        if input_dict["education"] not in ['College', 'PhD', 'Masters', 'High School']:
            raise ValueError("Invalid education value.")
        if input_dict["department"] not in ['Operations', 'Management', 'Administration', 'Sales', 'Engineering']:
            raise ValueError("Invalid department value.")
        if input_dict["seniority"] not in [1, 2, 3, 4, 5]:
            raise ValueError("Invalid seniority value. Seniority must be 1, 2, 3, 4, or 5.")

        # Input data
        input_df = pd.DataFrame.from_dict(input_dict, orient='index').T

        with open("./trained_model.pkl", "rb") as f:
            lm4_loaded = pickle.load(f)

        # Ensure data types are consistent with the model
        input_df['age'] = input_df['age'].astype(float)
        input_df['performance'] = input_df['performance'].astype(float)
        input_df['seniority'] = input_df['seniority'].astype(float)

        # Make prediction using the loaded model
        prediction = lm4_loaded.predict(exog=input_df, transform=True).values[0]

        return {"prediction": round(prediction, 2)}
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Model file not found")
    except KeyError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# En project: uvicorn main:app --reload