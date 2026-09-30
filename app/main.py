from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Docker Demo",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "FastAPI CI/CD is working"}


@app.get("/health")
def health():
    return {"status": "ok"}