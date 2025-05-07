from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
  return {"message": "Hello, Azure Web App!"}

@app.get("/square/{number}")
def get_square(number: int):
    return {"number": number, "square": number ** 2}
  

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
