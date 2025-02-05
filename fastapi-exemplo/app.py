import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from prometheus_fastapi_instrumentator import Instrumentator
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()





Instrumentator().instrument(app).expose(app)


@app.get("/")
async def root():
    return {"message": "Raiz"}


# Endpoint: /hello
@app.get("/hello")
async def hello(request: Request):
    # REQUEST_COUNT.labels(method=request.method).inc()
    return {"message": "Hello"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8080, reload=True)
