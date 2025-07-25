FROM python:3.12-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the project into the image
ADD . /app

# Set a default API key (can be overridden at runtime)
ENV NY_TIMES_API_KEY=""

# Sync the project into a new environment, using the frozen lockfile
WORKDIR /app

RUN uv venv .venv

RUN uv sync

EXPOSE 8080

CMD ["uv", "run", "fast_api_mcp_server/get_news_mcp.py"]