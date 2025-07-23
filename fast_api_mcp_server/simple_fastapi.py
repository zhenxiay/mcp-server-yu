from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hello")
def read_hello():
    return {"message": "Hello, world!"}

if __name__ == "__main__":
    uvicorn.run("simple_fastapi:app", host="0.0.0.0", port=8000, reload=True)