
from pydantic import BaseModel
from mcp.server.fastmcp import FastMCP
from test_ny_times import get_news_headers
import os

news_mcp = FastMCP(
                   name="News_MCP",
                   port=8001,
                   host="127.0.0.1",
                   stateless_http=True
                   )

@news_mcp.tool()
async def get_news(year: int = 2020, month: int = 1):
    """
    Get top headlines from New York Times REST API for a specific year and month.
    """
    return get_news_headers(year, month)

@news_mcp.tool()
async def hello_world():
    """
    A test tool which sends back Hello World when it gets called.
    """
    return {"message": "Hello, world!"}

if __name__ == "__main__":
    news_mcp.run(transport="streamable-http")
    