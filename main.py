from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")

def read_root():
    return {"message": "IoT Backend is running"}

@app.post("/send_data")
async def receive_data(request: Request):
    data = await request.json()
    print("Received Data:", data)
    return {"status": "Data received Sucessfully!"}