import uvicorn
from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    ALEXNET = "alexnet"
    RESNET = "resnet"
    LENET = "lenet"


app = FastAPI()


@app.get("/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.ALEXNET:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    elif model_name.value == "resnet":
        return {"model_name": model_name, "message": "Leaning ResNet!"}
    return {"model_name": model_name, "message": "Have some residuals!"}


def main():
    uvicorn.run("gpu_api:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
