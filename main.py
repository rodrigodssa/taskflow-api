from fastapi import FastAPI

app = FastAPI(title="TaskFlow API")

@app.get("/")
def home():
    return {"message": "TaskFlow API funcionando!"}
