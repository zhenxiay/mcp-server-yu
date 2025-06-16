from fastapi import FastAPI
from pydantic import BaseModel
from fastapi_mcp import FastApiMCP
from test_ny_times import get_news_headers
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

@app.get("/news", operation_id="get_news")
async def get_news(year: int = 2020, month: int = 1):
    """
    Get top headlines from New York Times REST API for a specific year and month.
    """
    return get_news_headers(year, month)

@app.get("/test", operation_id="hello_world", response_model=dict[str, str])
async def hello_world():
    return {"message": "Hello, world!"}

mcp = FastApiMCP(
    app,
    name="MCP_News_Server",
    description="Get top headlines from New York Times REST API",
)

mcp.mount()

if __name__ == "__main__":
    import uvicorn    
    uvicorn.run(app, host="127.0.0.1", port=8002)