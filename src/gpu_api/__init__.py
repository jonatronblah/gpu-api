import uvicorn
from fastapi import FastAPI
from enum import Enum
import subprocess


class TaskName(str, Enum):
    MESH = "mesh"


app = FastAPI()


@app.get("/{task_name}")
async def get_model(task_name: TaskName):
    if task_name is TaskName.MESH:
        result = subprocess.run(
            [
                "python3",
                "run.py",
                "configs/instant-mesh-large.yaml",
                "examples/img.jpg",
                "--export_texmap",
            ],
            capture_output=True,
            text=True,
        )

        return {"task_name": task_name, "result": result}


def main():
    uvicorn.run("gpu_api:app", host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
