from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    data = {
        "Owner": "Gautam",
        "Author": "Adani",
        "Additional_info": {  # You can add nested dictionaries here
            "key1": "SEZ Limited-01",
            "key2": "Airport Holdings ",
        }, 
    }
    return data


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
