from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    temperature: float

@app.get("/")

def read_root():
    return {"message": "IoT Backend is running"}

@app.post("/send_data")
async def receive_data(data:Data):
    print("Received Data:", data)
    return {"status": "Data received Sucessfully!"}