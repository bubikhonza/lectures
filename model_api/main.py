from typing import Union

from fastapi import FastAPI
import uvicorn
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from enum import Enum
import pandas as pd

import joblib


class SupportedModels(Enum):
    RANDOM_FOREST = "RandomForestClassifier"
    DECISION_TREE = "DecisionTreeClassifier"


class ModelHandler:
    LOADED_MODELS = {}

    @classmethod
    def load_model(cls, model: SupportedModels):
        if model == SupportedModels.RANDOM_FOREST:
            #TODO: Do not use absolute paths
            ModelHandler.LOADED_MODELS[SupportedModels.RANDOM_FOREST] = joblib.load(
                "J:\projects\lectures\model_api\models\model_random_forest.pkl")
        elif model == SupportedModels.DECISION_TREE:
            ModelHandler.LOADED_MODELS[SupportedModels.DECISION_TREE] = joblib.load(
                "J:\projects\lectures\model_api\models\model_dec_tree.pkl")
        else:
            raise Exception("No model with this name")

    @classmethod
    def get_model(cls, model: SupportedModels):
        return cls.LOADED_MODELS[model]

class InputData(BaseModel):
    Pclass: int
    Sex: int
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: float


app = FastAPI()

#TODO: change from deprecated
@app.on_event("startup")
def load_all_models():
    ModelHandler.load_model(SupportedModels.RANDOM_FOREST)
    ModelHandler.load_model(SupportedModels.DECISION_TREE)

@app.post("/predict/{model_name}")
def predict(model_name: SupportedModels, input_data: InputData):
    model = ModelHandler.get_model(model_name)
    input_df = pd.DataFrame([jsonable_encoder(input_data)])
    result = model.predict(input_df)
    return {"result": result.tolist()}


@app.get("/models")
def get_models():
    #TODO: implement
    return {"models": []}


@app.get("/models/{model_name}")
def get_model_info(model_name: str):
    # TODO: implement
    return {"name": model_name, "something": 20}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
